from flask import Flask, request, jsonify, make_response
import boto3
import config
import logging

app = Flask(__name__)

logging.basicConfig(filename=config.LOG_FILE, level=logging.INFO)

def create_client(aws_access_key_id, aws_secret_access_key, region_name):
    return boto3.client('ec2',
        aws_access_key_id=aws_access_key_id, 
        aws_secret_access_key=aws_secret_access_key, 
        region_name=region_name
    )

def ec2_list(aws_access_key_id, aws_secret_access_key, region_name):
    client = create_client(aws_access_key_id, aws_secret_access_key, region_name)
    try:
        response = client.describe_instances()
    except Exception as error:
        logging.error(error)
        raise Exception(error)
    instance_list = []
    for instances in response["Reservations"]:
        for instance in instances["Instances"]:
            for tag in instance["Tags"]:
                if tag["Key"].lower() == "name":
                    instance_name = tag["Value"]
                else:
                    instance_name = " "
            instance_list.append(
                {
                    "Name": instance_name,
                    "State": instance["State"]["Name"],
                    "InstanceId": instance["InstanceId"],
                    "InstanceType": instance["InstanceType"]
                }
            )
    return {"instances":instance_list}

def ec2_start(aws_access_key_id, aws_secret_access_key, region_name, InstanceIds):
    client = create_client(aws_access_key_id, aws_secret_access_key, region_name)
    try:
        response = client.start_instances(InstanceIds=InstanceIds)
    except Exception as error:
        logging.error(error)
        raise Exception(error)
    instance_list = []
    for instance in response["StartingInstances"]:
        instance_list.append(
            {
                "CurrentState": instance["CurrentState"]["Name"],
                "PreviousState": instance["PreviousState"]["Name"],
                "InstanceId": instance["InstanceId"],
            }
        )
    return {"instances":instance_list}

def ec2_stop(aws_access_key_id, aws_secret_access_key, region_name, InstanceIds):
    client = create_client(aws_access_key_id, aws_secret_access_key, region_name)
    try:
        response = client.stop_instances(InstanceIds=InstanceIds)
    except Exception as error:
        logging.error(error)
        raise Exception(error)
    instance_list = []
    for instance in response["StoppingInstances"]:
        instance_list.append(
            {
                "CurrentState": instance["CurrentState"]["Name"],
                "PreviousState": instance["PreviousState"]["Name"],
                "InstanceId": instance["InstanceId"],
            }
        )
    return {"instances":instance_list}

@app.route("/ec2/list", methods=["GET"])
def ec2_list_query_param():
    aws_access_key_id = request.args.get("aws_access_key_id")
    aws_secret_access_key = request.args.get("aws_secret_access_key")
    region_name = request.args.get("region_name")
    if region_name is None or region_name==" "  or region_name=="":
        region_name = "eu-central-1"
    if (aws_access_key_id is None or aws_secret_access_key is None):
        return make_response(jsonify(response=f"Missing Parameters."), 400)
    else:
        try:
            response = ec2_list(aws_access_key_id, aws_secret_access_key, region_name)
        except Exception as error:
            return make_response(jsonify(response=str(error)), 500)
        return response

@app.route("/ec2/start", methods=["POST"])
def ec2_start_query_param():
    aws_access_key_id = request.args.get("aws_access_key_id")
    aws_secret_access_key = request.args.get("aws_secret_access_key")
    region_name = request.args.get("region_name")
    json_body = request.get_json(force=True)
    InstanceIds = json_body["InstanceIds"]
    if region_name is None or region_name==" "  or region_name=="":
        region_name = "eu-central-1"
    if (aws_access_key_id is None or aws_secret_access_key is None):
        return make_response(jsonify(response=f"Missing Parameters."), 400)
    else:
        try:
            response = ec2_start(aws_access_key_id, aws_secret_access_key, region_name, InstanceIds)
        except Exception as error:
            return make_response(jsonify(response=str(error)), 500)
        return response

@app.route("/ec2/stop", methods=["POST"])
def ec2_stop_query_param():
    aws_access_key_id = request.args.get("aws_access_key_id")
    aws_secret_access_key = request.args.get("aws_secret_access_key")
    region_name = request.args.get("region_name")
    json_body = request.get_json(force=True)
    InstanceIds = json_body["InstanceIds"]
    if region_name is None or region_name==" "  or region_name=="":
        region_name = "eu-central-1"
    if (aws_access_key_id is None or aws_secret_access_key is None):
        return make_response(jsonify(response=f"Missing Parameters."), 400)
    else:
        try:
            response = ec2_stop(aws_access_key_id, aws_secret_access_key, region_name, InstanceIds)
        except Exception as error:
           return make_response(jsonify(response=str(error)), 500)
        return response

@app.route("/ec2/list/<aws_access_key_id>/<aws_secret_access_key>/<region_name>", methods=["GET"])
def ec2_list_url_param(aws_access_key_id, aws_secret_access_key, region_name):
    try:
        response = ec2_list(aws_access_key_id, aws_secret_access_key, region_name)
    except Exception as error:
        return make_response(jsonify(response=str(error)), 500)
    return response

@app.route("/ec2/start/<aws_access_key_id>/<aws_secret_access_key>/<region_name>", methods=["POST"])
def ec2_start_url_param(aws_access_key_id, aws_secret_access_key, region_name):
    json_body = request.get_json(force=True)
    InstanceIds = json_body["InstanceIds"]
    try:
        response = ec2_start(aws_access_key_id, aws_secret_access_key, region_name, InstanceIds)
    except Exception as error:
        return make_response(jsonify(response=str(error)), 500)
    return response

@app.route("/ec2/stop/<aws_access_key_id>/<aws_secret_access_key>/<region_name>", methods=["POST"])
def ec2_stop_url_param(aws_access_key_id, aws_secret_access_key, region_name):
    json_body = request.get_json(force=True)
    InstanceIds = json_body["InstanceIds"]
    try:
        response = ec2_stop(aws_access_key_id, aws_secret_access_key, region_name, InstanceIds)
    except Exception as error:
        return make_response(jsonify(response=str(error)), 500)
    return response

if __name__=="__main__":
    app.run(host=config.HOST, port=config.PORT)