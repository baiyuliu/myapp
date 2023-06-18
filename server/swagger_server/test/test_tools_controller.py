# coding: utf-8

#from __future__ import absolute_import

from flask import json
#from six import BytesIO

from swagger_server.models.handler_validate_ip_request import HandlerValidateIPRequest  # noqa: E501
#from swagger_server.models.handler_validate_ip_response import HandlerValidateIPResponse  # noqa: E501
#from swagger_server.models.model_query import ModelQuery  # noqa: E501
#from swagger_server.models.utils_http_error import UtilsHTTPError  # noqa: E501
from swagger_server.test import BaseTestCase


class TestToolsController(BaseTestCase):
    """ToolsController integration test stubs"""

    def test_lookup_domain(self):
        """Test case for lookup_domain

        Lookup domain
        """
        query_string = [('domain', 'domain_example')]
        response = self.client.open(
            '/v1/tools/lookup',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_validate_ip(self):
        """Test case for validate_ip

        Simple IP validation
        """
        body = HandlerValidateIPRequest()
        response = self.client.open(
            '/v1/tools/validate',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
