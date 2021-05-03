# background function
# curl localhost:8080 -X POST -H "Content-Type: application/json" -d '{"event":{"@type":"type.googleapis.com/google.pubsub.v1.PubsubMessage","attributes":{"attr1":"attr1-value"},"data":"d29ybGQ="},"context":{"eventId":"1144231683168617","timestamp":"2020-05-06T07:33:34.556Z","eventType":"google.pubsub.topic.publish","resource":{"service":"pubsub.googleapis.com","name":"projects/sample-project/topics/gcf-test","type":"type.googleapis.com/google.pubsub.v1.PubsubMessage"}}}'

def hello_pubsub(event, context):
    import base64

    print('Function was triggered by messageId {} published at {}'.format(context.event_id, context.timestamp))

    if 'data' in event:
        name = base64.b16encode(event['data']).decode('utf-8')
    else:
        name = 'World'

    print('Hello {}!'.format(name))