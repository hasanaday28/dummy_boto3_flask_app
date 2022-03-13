# Dummy Boto3 Flask App

## Config File (config.py)
HOST=<your_host>
PORT=<your_port>
LOG_FILE=<your_log>

## Endpoints
### with Query Parameters and JSON Body
#### /ec2/list?aws_access_key_id=<your_aws_access_key_id>&aws_secret_access_key=<your_aws_secret_access_key>&region_name=<your_region_name>
#### /ec2/start?aws_access_key_id=<your_aws_access_key_id>&aws_secret_access_key=<your_aws_secret_access_key>&region_name=<your_region_name>
##### Body (JSON)
    {
        "InstanceIds": [
            "<InstanceId>",
        ]
    }
#### /ec2/stop?aws_access_key_id=<your_aws_access_key_id>&aws_secret_access_key=<your_aws_secret_access_key>&region_name=<your_region_name>
##### Body (JSON)
    {
        "InstanceIds": [
            "<InstanceId>",
        ]
    }

### with URL Parameters and JSON Body
#### /ec2/list/<aws_access_key_id>/<aws_secret_access_key>/<region_name>
#### /ec2/start/<aws_access_key_id>/<aws_secret_access_key>/<region_name>
##### Body (JSON)
    {
        "InstanceIds": [
            "<InstanceId>",
        ]
    }
#### /ec2/stop/<aws_access_key_id>/<aws_secret_access_key>/<region_name>
##### Body (JSON)
    {
        "InstanceIds": [
            "<InstanceId>",
        ]
    }