from json import dumps


def index(event, context):
    body = {"message": "Your function executed successfully!", "input": event}

    response = {"statusCode": 200, "body": dumps(body)}

    return response
