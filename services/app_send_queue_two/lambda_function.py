import json
import requests
import logging
import os

from sqs_service import SqsService

API_URI = 'https://random-data-api.com/api/v2/banks'
SQS_SEND_QUEUE_ONE_URL = ''


def lambda_handler(event, context):
    try:
        log_level = os.getenv('LOG_LEVEL', 'INFO')
        logging.getLogger().setLevel(log_level)
        process_message(event=event)
    except Exception as ex:
        logging.error(str(ex))


def process_message(event: dict):
    for record in event['Records']:
        body = json.loads(record["body"])
        isStartSession = body["StartSession"]
        logging.info(f'Start the session')

        try:

            if isStartSession:
              response = requests.get(API_URI)
              if response.ok == False:
                 raise Exception("Response API failed")

              response_dict = json.loads(response.text)
              routing_number = float(response_dict['routing_number'])
              message = { "CurrentValue": routing_number }
              send_message(message)

        except Exception as ex:
            logging.error(str(ex))


def send_message(record: dict):
    sqsService = SqsService
    sqsService.send_messager_to_queue(SQS_SEND_QUEUE_ONE_URL, record['body'])
    sqsService.delete_current_messager(SQS_SEND_QUEUE_ONE_URL, record['receiptHandle'])
