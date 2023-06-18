import unittest
from unittest.mock import patch, call
from swagger_server.controllers import history_controller

class QueriesControllerTest(unittest.TestCase):
    @patch('swagger_server.controllers.history_controller.get_latest_queries')
    @patch('swagger_server.controllers.history_controller.logging')
    def test_queries_history(self, mock_logging, mock_get_latest_queries):
        # Mock the return value of get_latest_queries()
        mock_get_latest_queries.return_value = [
            ('example.com', ['192.168.0.1', '192.168.0.2']),
            ('google.com', ['8.8.8.8', '8.8.4.4'])
        ]

        # Call the function under test
        result = history_controller.queries_history()

        # Assert the expected result
        expected_result = [
            ('example.com', ['192.168.0.1', '192.168.0.2']),
            ('google.com', ['8.8.8.8', '8.8.4.4'])
        ]
        self.assertEqual(result, expected_result)

        # Assert that the logging calls were made correctly
        expected_logs = [
            call("data: %s", ('example.com', ['192.168.0.1', '192.168.0.2'])),
            call('Domain: %s', 'example.com'),
            call("IPv4 Addresses: %s", ['192.168.0.1', '192.168.0.2']),
            call('---'),
            call("data: %s", ('google.com', ['8.8.8.8', '8.8.4.4'])),
            call('Domain: %s', 'google.com'),
            call("IPv4 Addresses: %s", ['8.8.8.8', '8.8.4.4']),
            call('---')
        ]
        mock_logging.info.assert_has_calls(expected_logs)

if __name__ == '__main__':
    unittest.main()
