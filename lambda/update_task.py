import json
import os
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def handler(event, context):
    task_id = event['pathParameters']['taskId']
    body = json.loads(event['body'])

    result = table.update_item(
        Key={'taskId': task_id},
        UpdateExpression="set title = :t, description = :d, #s = :s",
        ExpressionAttributeValues={
            ':t': body['title'],
            ':d': body['description'],
            ':s': body['status'],
        },
        ExpressionAttributeNames={
            "#s": "status"
        },
        ReturnValues="ALL_NEW"
    )

    return {
        'statusCode': 200,
        'body': json.dumps(result['Attributes'])
    }
