import unittest
from pyndemic.core.api import RequestTypes, ResponseTypes, \
    GameplayCommands, termination_request, empty_response, \
    final_response, message_response


class APITestCase(unittest.TestCase):
    def test_termination_request(self):
        response = termination_request()
        required = RequestTypes.TERMINATION.value
        self.assertEqual(response['type'], required)

    def test_empty_response(self):
        response = empty_response()
        required = ResponseTypes.EMPTY.value
        self.assertEqual(response['type'], required)

    def test_final_response(self):
        message = "see ya"
        response = final_response(message)
        required = ResponseTypes.TERMINATION.value
        self.assertEqual(response['type'], required)
        self.assertEqual(response['message'], message)

    def test_message_response(self):
        message = "something to say"
        response = message_response(message)
        required = ResponseTypes.MESSAGE.value
        self.assertEqual(response['type'], required)
        self.assertEqual(response['message'], message)

