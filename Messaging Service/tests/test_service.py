from temp_messenger.service import MessageService, WebServer


def test_service_names():
    assert MessageService.name == 'message_service'
    assert WebServer.name == 'web_server'
