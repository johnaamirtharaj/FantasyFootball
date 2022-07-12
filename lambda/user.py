import boto3
import uuid



def lambda_handler(event, context):
    # TODO implement
    #exports.handler = async (event) => {
    print("Received event ",event)
    # print (event.field)
    # print (event.arguments)
    user = {
            'userid': userid,
            'usertype': usertype,
            'username': uname,
            'points':point
    }
    
    dynamodb = boto3.resource(
        'dynamodb', endpoint_url="https://dynamodb.us-east-1.amazonaws.com")
    # Specify the table
    users_table = dynamodb.Table('Users')
    response = users_table.put_item(
        # Data to be inserted
        Item=user
    )
    print(response)
    return (response)