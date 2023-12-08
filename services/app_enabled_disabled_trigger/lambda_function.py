import json
import requests
import logging
import os
import boto3

session = boto3.Session(
    aws_access_key_id=os.environ["ACCESS_KEY"],
    aws_secret_access_key=os.environ["SECRET_KEY"]
)
client = session.client('lambda')

def lambda_handler(event, context):
    try:
        log_level = os.getenv('LOG_LEVEL', 'INFO')
        logging.getLogger().setLevel(log_level)
        process_message(event=event)
    except Exception as ex:
        logging.error(str(ex))


def process_message(event):
    try:
      body = json.loads(event['body'])
      logging.info(f'Start enable or disable trigger lambda api')
      
      response = client.update_event_source_mapping(
      BatchSize=10,
      Enabled=False,
      FunctionName='app-process-queue-one',
      UUID='2003d51f-9712-40d4-a7a9-8369619b45f8',
)

    except Exception as ex:
        logging.error(str(ex))


def set_lambda_event_soursing(value, table):
    logging.info(f'Table: {table} - Value: {value}')
