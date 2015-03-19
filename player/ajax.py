import json

def sayhello(request):
    return json.dumps({'message':'Hello World'})

