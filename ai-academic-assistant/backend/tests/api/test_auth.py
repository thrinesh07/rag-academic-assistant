def test_register(client):
    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@example.com",
            "password": "strongpassword"
        }
    )
    assert response.status_code == 200
    assert response.json()["success"] is True


def test_login(client):
    client.post(
        "/api/v1/auth/register",
        json={
            "email": "login@example.com",
            "password": "strongpassword"
        }
    )

    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": "login@example.com",
            "password": "strongpassword"
        }
    )

    assert response.status_code == 200
    assert response.cookies.get("access_token") is not None


def test_invalid_login(client):
    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": "wrong@example.com",
            "password": "wrongpass"
        }
    )

    assert response.status_code == 401