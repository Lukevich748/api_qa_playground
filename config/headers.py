import os
from dotenv import load_dotenv

load_dotenv()


class Headers:

    def basic(self, x_task_id: str) -> dict:
        return {
            "Authorization": f"Bearer {os.getenv('TOKEN')}",
            "X-Task-Id": f"{x_task_id}"
        }
