import json
import uuid
import os
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def handler(event, context):
    body = json.loads(event['body'])
    item = {
        'taskId': str(uuid.uuid4()),
        'title': body['title'],
        'description': body['description'],
        'status': body.get('status', 'pending')
    }
    table.put_item(Item=item)

    return {
        'statusCode': 201,
        'body': json.dumps(item)
    }
