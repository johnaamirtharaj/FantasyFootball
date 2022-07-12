import boto3
import uuid



def lambda_handler(event, context):
    # TODO implement
    #exports.handler = async (event) => {
    print("Received event ",event)
    # print (event.field)
    # print (event.arguments)
    userid = uuid.uuid4()
    usertype = event["usertype"]
    uname = event["uname"]
    point = event["point"]
    
    
    dynamodb = boto3.resource(
        'dynamodb', endpoint_url="https://dynamodb.us-east-1.amazonaws.com")
    # Specify the table
    users_table = dynamodb.Table('Users')
    response = users_table.put_item(
        # Data to be inserted
        Item={
            'userid': str(userid),
            'usertype': usertype,
            'username': uname,
            'points':point
        }
    )
    print(response)
    return (response)