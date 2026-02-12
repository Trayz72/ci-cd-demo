def test_home_page(client):
    """Check if login page loads"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Login Page" in response.data

def test_successful_login(client):
    """Check login with correct credentials"""
    response = client.post("/", data={"username": "admin", "password": "secret"})
    assert b"Login successful!" in response.data

def test_failed_login(client):
    """Check login with wrong credentials"""
    response = client.post("/", data={"username": "user", "password": "wrong"})
    assert b"Login failed." in response.data
