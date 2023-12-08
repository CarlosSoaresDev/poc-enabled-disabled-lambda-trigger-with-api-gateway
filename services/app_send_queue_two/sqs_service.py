import json
import string
import boto3
import os

session = boto3.Session(
    aws_access_key_id=os.environ["ACCESS_KEY"],
    aws_secret_access_key=os.environ["SECRET_KEY"]
)
sqs = session.client('sqs')

class SqsService:

    def send_messager_to_queue(sqs_queue_url: string, message_body: dict):
        sqs.send_message(
            QueueUrl = sqs_queue_url,
            MessageBody = json.dumps(message_body)
        )

    def delete_current_messager(sqs_queue_url:string, receipt_handle: string):
        sqs.delete_message(
            QueueUrl = sqs_queue_url,
            ReceiptHandle = receipt_handle
        )
