#! /usr/bin/python
import json
import requests

url = 'http://localhost:80/mary'

#Abrir y leer json
with open ('/home/administradorcito/introduction-quiz/introduction_quiz.json') as qz:
     qui = json.load(qz)
print(qui)

#read = requests.post(url, qui=json.dumps(qui))

#curl -i -X POST --data @introduction_quiz.json http://localhost:80
