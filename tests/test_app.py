def test_get_home(web_client):
    response = web_client.get("/")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "I am a CI-CD hero!"

def test_get_greet(web_client):
    response = web_client.get("/greet/testname")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Hello, testname!"