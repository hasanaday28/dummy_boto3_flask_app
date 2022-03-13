# Dummy Boto3 Flask App

## Config File (config.py)
HOST=<your_host><br/>
PORT=<your_port><br/>
LOG_FILE=<your_log>

## Endpoints

### with Query Parameters and JSON Body

#### Endpoint: /ec2/list
##### Query Parameters
aws_access_key_id=<your_aws_access_key_id><br/>
aws_secret_access_key=<your_aws_secret_access_key><br/>
region_name=<your_region_name>

#### Endpoint: /ec2/start
##### Query Parameters
aws_access_key_id=<your_aws_access_key_id><br/>
aws_secret_access_key=<your_aws_secret_access_key><br/>
region_name=<your_region_name>
##### Body (JSON)
    {
        "InstanceIds": [
            "<InstanceId>",
        ]
    }

#### Endpoint: /ec2/stop
##### Query Parameters
aws_access_key_id=<your_aws_access_key_id><br/>
aws_secret_access_key=<your_aws_secret_access_key><br/>
region_name=<your_region_name>
##### Body (JSON)
    {
        "InstanceIds": [
            "<InstanceId>",
        ]
    }

### with Query Parameters and JSON Body

#### Endpoint: /ec2/list/<aws_access_key_id>/<aws_secret_access_key>/<region_name>

#### Endpoint: /ec2/start/<aws_access_key_id>/<aws_secret_access_key>/<region_name>
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