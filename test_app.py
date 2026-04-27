from app import app

def test_home_page():
    tester = app.test_client()
    response = tepyhtoster.get("/")
    assert response.status_code == 200