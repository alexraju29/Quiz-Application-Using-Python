import requests
parameter = {
    "amount": 10,
    "category": 18,
    "difficulty": "easy",
    "type": "boolean"
}
try:
    response = requests.get(url="https://opentdb.com/api.php", params=parameter)

except requests.exceptions.ConnectionError:

    question_data = [
        {
            "question": "Error 404\n Network not found",
            "correct_answer": "False",
        }

    ]
else:
    data = response.json()
    question_data = data["results"]
