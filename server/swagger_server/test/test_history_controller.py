# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

#from swagger_server.models.model_query import ModelQuery  # noqa: E501
#from swagger_server.models.utils_http_error import UtilsHTTPError  # noqa: E501
from swagger_server.test import BaseTestCase


class TestHistoryController(BaseTestCase):
    """HistoryController integration test stubs"""

    def test_queries_history(self):
        """Test case for queries_history

        List queries
        """
        response = self.client.open(
            '/v1/history',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))



if __name__ == '__main__':
    import unittest
    unittest.main()
