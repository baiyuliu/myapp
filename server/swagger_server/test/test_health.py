import unittest
from unittest.mock import MagicMock
from swagger_server.controllers.health_controller import health_check

class TestHealthCheck(unittest.TestCase):
    def test_health_check(self):
        # 调用 health_check 函数
        response = health_check()

        # 断言返回的结果是否正确
        self.assertEqual(response, 'application health!')

if __name__ == '__main__':
    unittest.main()

