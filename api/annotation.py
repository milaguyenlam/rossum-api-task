from flask import Blueprint, request
from services.annotation_service import export_annotation_service

annotation_route = Blueprint("annotation_route", __name__)


@annotation_route.route("/export/<int:queue_id>/<int:annotation_id>", methods=["POST"])
def export(queue_id, annotation_id):
    return export_annotation_service(queue_id=queue_id, annotation_id=annotation_id)
