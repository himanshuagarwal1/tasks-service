import json
import os
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def handler(event, context):
    task_id = event['pathParameters']['taskId']
    result = table.get_item(Key={'taskId': task_id})

    if 'Item' not in result:
        return {
            'statusCode': 404,
            'body': json.dumps({'error': 'Task not found'})
        }

    return {
        'statusCode': 200,
        'body': json.dumps(result['Item'])
    }
