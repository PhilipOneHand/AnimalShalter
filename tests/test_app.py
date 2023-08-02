import requests

def test_ping_server():

    url = 'http://192.168.32.3:5000/'

    # Send a GET request to the server
    response = requests.get(url)

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"





