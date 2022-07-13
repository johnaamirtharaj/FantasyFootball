import boto3
import uuid
import json
import base64


def lambda_handler(event, context):
    # TODO implement
    #exports.handler = async (event) => {
    print("Received event ",event)
    for i in event['Records']:
        print(i)
        print(i["kinesis"]["data"])
        enc = i["kinesis"]["data"]
        dec = base64.b64decode(enc)
        print(dec.decode('utf-8'))
        dec = dec.decode('utf-8')
        event = json.loads(dec)
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