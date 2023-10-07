#to fetch questions from opentdb API

import requests
from requests import *

parameter = {
    "amount": 10,
    "type": "boolean"
}
response = requests.get(url="https://opentdb.com/api.php", params=parameter)
response.raise_for_status()


api_question = response.json()

question_data = api_question["results"]


