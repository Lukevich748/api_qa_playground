import os

HOST = "https://dev-gs.qa-playground.com/api/v1" if os.environ["STAGE"] == "DEV" else "https://release-gs.qa-playground.com/api/v1"


class Endpoints:

    get_all_users = f"{HOST}/users"