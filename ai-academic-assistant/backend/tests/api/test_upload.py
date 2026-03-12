from io import BytesIO


def test_upload_requires_admin(client):

    # Register normal user
    client.post(
        "/api/v1/auth/register",
        json={
            "email": "user@example.com",
            "password": "strongpassword"
        }
    )

    file_data = BytesIO(b"Fake PDF content")

    response = client.post(
        "/api/v1/upload/",
        data={"subject": "OS"},
        files={"file": ("test.pdf", file_data, "application/pdf")}
    )

    # Should fail because not admin
    assert response.status_code == 403