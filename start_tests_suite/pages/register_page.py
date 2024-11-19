from selene import browser, have
import requests


def test_create_test_email():
    url = "https://privatix-temp-mail-v1.p.rapidapi.com/request/mail/id/null/"

    headers = {
        "x-rapidapi-key": "Sign Up for Key",
        "x-rapidapi-host": "privatix-temp-mail-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    print(response.json())


