import requests


class MyLittleEndpointClient:
    url = "https://my-little-endpoint.ok/rossum"

    def __init__(self) -> None:
        pass

    def send_annotation(self, annotation_id, content):
        try:
            response = requests.post(
                url=self.url, json={"annotationId": annotation_id, "content": content}
            )
            return response.ok
        except:
            return False
