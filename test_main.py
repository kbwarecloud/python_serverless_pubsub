import base64

import mock

import main

context = mock.Mock()
context.event_id = '617187464135194'
context.timestamp = '2019-07-15T22:09:03.761Z'

def test_print_hello_world(capsys):
    event = {}

    main.hello_pubsub(event, context)

    out, err = capsys.readouterr()
    assert 'Hello World!' in out


def test_print_hello_custom(capsys):
    name = 'Custom'
    event = {
        'data': base64.b64encode(name.encode())
    }

    main.hello_pubsub(event, context)

    out, err = capsys.readouterr()
    assert 'Hello {}!'.format(name) in out


