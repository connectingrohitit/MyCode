from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
items = 'Test'
client = MongoClient("Connection String")
db = client["TestDB"]
coll = db["MyDBCollection"]
data1 = coll.find_one()
# list1 = list(data1)
print(data1)
# for row in data1:
#     print(row)


@app.get('/get-one')
def get_one():
    return {"items": items}
