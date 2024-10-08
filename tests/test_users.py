from config.base_test import BaseTest


class TestUsers(BaseTest):


    def test_get_all_users(self):
        self.api_users.get_all_users("API-1")