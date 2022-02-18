from flask import make_response
from rossum.lib.api_client import RossumClient
import utils.xml_util
import os
import config
import base64
from utils.my_little_endpoint_client import MyLittleEndpointClient


def export_annotation_service(queue_id, annotation_id):
    try:
        with RossumClient(
            context=None,
            username=config.rossum_username,
            password=config.rossum_password,
            url="https://api.elis.rossum.ai/v1",
        ) as rossum_client:
            response = rossum_client.get(f"queues/{queue_id}/export?format=xml&id={annotation_id}")
            if not response.ok:
                raise ValueError(f"Failed to export: {response.status_code}")
            converted_xml_string = utils.xml_util.export_annotation_validate_and_transform(
                response.content
            )
            encoded_xml_string = base64.encode(bytes(converted_xml_string, encoding="utf-8"))
            return {
                "success": MyLittleEndpointClient().send_annotation(
                    annotation_id, encoded_xml_string
                ),
            }

    except Exception as e:
        return make_response({"message": str(e)}, 404)
