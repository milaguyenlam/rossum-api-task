from flask import make_response
from rossum.lib.api_client import RossumClient
import utils.xml_util
import config
import base64
from utils.my_little_endpoint_client import MyLittleEndpointClient
from flask import current_app as app


def export_annotation_service(queue_id, annotation_id):
    try:
        with RossumClient(
            context=None,
            user=config.rossum_username,
            password=config.rossum_password,
            url="https://api.elis.rossum.ai/v1",
        ) as rossum_client:
            response = rossum_client.get(f"queues/{queue_id}/export?format=xml&id={annotation_id}")
            if not response.ok:
                raise ValueError(
                    f"Failed to export queueId={queue_id} annotationId={annotation_id}: {response.status_code}"
                )
            app.logger.info(f"response from rossum api:\n {response.text}")
            converted_xml_string = utils.xml_util.export_annotation_validate_and_transform(
                response.content
            )
            app.logger.info(f"converted xml:\n {converted_xml_string}")
            encoded_xml_string = base64.b64encode(converted_xml_string).decode("utf-8")
            return {
                "success": MyLittleEndpointClient().send_annotation(
                    annotation_id, encoded_xml_string
                ),
            }
    except Exception as e:
        message = f"type {type(e).__name__} : {e}"
        app.logger.error(message)
        return make_response({"message": message}, 404)
