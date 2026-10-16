from app import app

def test_home():
  client = app.test_client()


  response = client.get("/")

  assert response.status_code == 200
  assert response.json == {
      "message": "Hello! My CI/CD pipeline is working."
  }

def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json == {"status": "healthy"}


