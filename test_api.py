import requests

def test_check_if_the_website_online():
    response = requests.get("http://127.0.0.1:5000/students/")

    assert response.status_code == 200

def test_adding_students():

    test_user = {"name": "Test User"}
    response = requests.post("http://127.0.0.1:5000/add-students", json= test_user)


    assert response.status_code == 200    