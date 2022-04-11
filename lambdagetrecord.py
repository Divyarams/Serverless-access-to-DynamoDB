import json
import boto3

dynamo = boto3.client('dynamodb')


    

def lambda_handler(event, context):
    print('Event recieved:'+ json.dumps(event))
    operation = event['httpMethod']
    id = event['queryStringParameters']['id']
    table = event['pathParameters']['proxy']
    table1 = str(table)
    print ('the id is:'+ id)
    print ('the name is:'+ table1)
    if operation =='GET':
        res1 = dynamo.get_item(
            TableName= table,
            Key= {'id': {
                'S': id }
                }
                )
    return {
        'statusCode': '200',
        'body':json.dumps(res1),
        'headers': {
            'Content-Type': 'application/json',
        }
    }  