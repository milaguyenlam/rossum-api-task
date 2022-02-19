from app import create_app
import json


def test_export():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.get(
            "/export/174602/12281537",
            headers={"Authorization": "Basic bXlVc2VyMTIzOnNlY3JldFNlY3JldA=="},
        )
        assert response.status_code == 200
        assert json.loads(response.data)["success"] == True
