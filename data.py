import requests


def get_questions():
    parameters = {
        "amount": 10,
        "type": "boolean",
    }
    response = requests.get("https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    return response.json()["results"]


question_data = get_questions()


