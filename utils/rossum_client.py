import os
import requests
from app import app

# WARNING: There is an official RossumClient available and should be used instead
class RossumClient:
    headers = {"Content-Type": "application/json; charset=utf-8"}
    base_url = "https://api.elis.rossum.ai"

    def __init__(
        self, username=os.environ("ROSSUM_API_USERNAME"), password=os.environ("ROSSUM_API_PASSWORD")
    ) -> None:
        self.token = self.authenticate(username, password)

    def authenticate(self, username, password):
        response = requests.post(
            url=f"{self.base_url}/v1/auth/login",
            headers=self.headers,
            data={"username": username, "password": password},
        )
        if response.ok:
            return response.content["key"]
        else:
            app.logger.error(f"Couldn't login to Rossum - status code: {response.status_code}")
            return None

    def export_annotation(self, queue_id, annotation_id, format):
        if format not in ["csv", "json", "xml"]:
            raise Exception(
                f'export_annotation(...) format parameter expects values from ["csv", "json", "xml"] but {format} was passed.'
            )
        response = requests.get(
            url=f"{self.base_url}/v1/queues/{queue_id}/export?format={format}&id={annotation_id}",
            headers={f"Authorization: token {self.token}"},
        )
        if response.ok:
            return response.content
        else:
            app.logger.error(
                f"Couldn't export annotation (queue_id={queue_id},annotation_id={annotation_id}) - status code: {response.status_code}"
            )
            return None
