import allure
import requests
from config.headers import Headers
from services.users.endpoints import Endpoints
from services.users.payloads import Payloads
from utils.helper import Helper


class UsersAPI(Helper):

    def __init__(self):
        self._endpoints = Endpoints()
        self._headers = Headers()
        self._payloads = Payloads()

    @allure.step("Get All Users")
    def get_all_users(self, x_task_id, offset=0, limit=10, expected_result=True):
        response = requests.get(
            url=self._endpoints.get_all_users,
            headers=self._headers.basic(x_task_id=x_task_id),
            params={
                "offset": offset,
                "limit": limit
            },
        )
        self.attach_response(response.json())
        if expected_result:
            assert response.status_code == 200, response.json()