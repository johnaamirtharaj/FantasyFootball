import boto3
from botocore.exceptions import ClientError



def lambda_handler(event, context):

    print("Received event ",event)

    userid = event["userid"]
   
    
    
    dynamodb = boto3.resource(
        'dynamodb', endpoint_url="https://dynamodb.us-east-1.amazonaws.com")
    # Specify the table
    users_table = dynamodb.Table('Users')
    try:
        response = users_table.get_item(
            Key={'userid': userid})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']
    



