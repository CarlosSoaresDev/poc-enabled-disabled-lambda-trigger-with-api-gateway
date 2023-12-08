import json
import string
import requests
import logging
import os

API_URI = 'https://random-data-api.com/api/v2/banks'

def lambda_handler(event, context):
    try:
        log_level = os.getenv('LOG_LEVEL', 'INFO')
        logging.getLogger().setLevel(log_level)
        process_message(event=event)
    except Exception as ex:
        logging.error(str(ex))

def process_message(event: dict) -> None:
    for record in event['Records']:
        body = json.loads(record["body"])
        isStartSession = body["StartSession"]
        logging.info(f'Start an new session')

        try:
            if isStartSession:
               response = requests.get(API_URI)
               if response.ok == False:
                   raise Exception("Response API failed")

               response_dict = json.loads(response.text)
               routing_number = float(response_dict['routing_number'])

               set_value_database("table_insert_2", routing_number)

        except Exception as ex:
            logging.error(str(ex))

def set_value_database(table: string, value: float) -> None:
    logging.info(f'Table: {table} - Value: {value}')
