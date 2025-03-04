import os
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def handler(event, context):
    task_id = event['pathParameters']['taskId']
    table.delete_item(Key={'taskId': task_id})

    return {
        'statusCode': 204,
        'body': ''
    }
