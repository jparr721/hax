import requests

"""
Brute-force checks for user accounts given a particular naming format for an email system
"""

def addToFile(data):
    f = open("matches.txt", "w+")
    f.write(data)
    f.close()

with open("names.txt") as f:
    content = f.readlines()

names = [x.strip() for x in content]

url = 'ADD HERE'

for name in list:
    email = name + "@EMAILDOMAIN"    
    r = requests.post(url, data={'email': email})
    if r.json()['statusCode'] == 200:
        addToFile(email)
