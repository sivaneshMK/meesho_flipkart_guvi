import requests


def test_api():
    params = {"num1":43, "num2":3}
    response = requests.get(url="https://fastapi-calculadora.onrender.com/calculo-basico/sumar/", params=params)
    print(response.status_code)
    assert response.status_code==200, "Test passed"
    print(response.content)