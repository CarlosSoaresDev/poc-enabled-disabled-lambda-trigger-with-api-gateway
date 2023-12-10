import json
import logging
import os
import boto3

session = boto3.Session(
    aws_access_key_id=os.environ["ACCESS_KEY"],
    aws_secret_access_key=os.environ["SECRET_KEY"]
)

client = session.client('lambda')

def lambda_handler(event, context):

    log_level = os.getenv('LOG_LEVEL', 'INFO')
    logging.getLogger().setLevel(log_level)        
    
    try:
       services = json.loads(event['body'])
       logging.info(f'Start enable or disable trigger lambda api')
       data_response = []

       for service in  services["Services"]:      
          response_client = client.update_event_source_mapping(Enabled=service["Enabled"], UUID=service["UUID"])
          data_response.append(response_client["EventSourceArn"].split(":")[-1])

       return {
            "statusCode": 200,
            "body": json.dumps(data_response)
        }

    except Exception as ex:
        logging.error(str(ex))


def set_lambda_event_soursing(value, table):
    logging.info(f'Table: {table} - Value: {value}')
