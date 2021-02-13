import json

from bson import json_util
from flask import Flask, request, render_template, jsonify
import pymongo

app = Flask(__name__)
print(__name__)

# MongoDb connection
connection_string = "mongodb+srv://sa:rrfYrY3mSzHSgzJR@cluster0.qa3t4.mongodb.net/sample_restaurants?retryWrites=true&w=majority"
myclient = pymongo.MongoClient(connection_string)
db = myclient.sample_restaurants
cRestaurants = db["restaurants"]


# http://127.0.0.1:5001/
@app.route("/", methods=["GET"])
def hello():
    return "<h1>Welcome to Python Flask Example</h1>"


# http://127.0.0.1:5001/hello
@app.route("/hello", methods=["GET"])
def greet():
    return "<h1>Hello World</h1>"

# Return JSON Response as an API
# http://127.0.0.1:5001/person
@app.route("/person", methods=["GET"])
def person():
    people = [{'name': 'Alice', 'birth_year': 1986},
              {'name': 'Bob', 'birth_year': 1985}]
    jsonResponse = jsonify(people)
    return jsonResponse

# Read Query parameter
# http://127.0.0.1:5001/name
# http://127.0.0.1:5001/name?value=pritesh
# This should return your name
@app.route("/name", methods=["GET"])
def name():
    if(request.args.get("value")):
        return "<h1>" + request.args.get("value") + "</h1>"

    return "<h1>Pritesh Patel</h1>"


# path parameter example
# http://127.0.0.1:5001/hello/pritesh/lambton
@app.route('/hello/<user>/<org>')
def hello_name(user, org):
    return render_template('hello.html', name=user, org=org)

# path parameter example
# http://127.0.0.1:5001/restaurants/American
# http://127.0.0.1:5001/restaurants/Chinese
@app.route('/restaurants/<cuisine>', methods=["POST"])
def restaurants_cuisine(cuisine):
    columns = {"restaurant_id", "name", "cuisine", "borough", "cuisine"}
    results = cRestaurants.find({'cuisine': cuisine}, columns)
    details_dicts = [doc for doc in results]
    json_docs = toJson(details_dicts) # Convert to JSON
    return json_docs


# Utility Function
def toJson(data):
    """Convert Mongo object(s) to JSON"""
    return json.dumps(data, default=json_util.default)

# http://127.0.0.1:5001/t1
@app.route("/t1")
def template_test():
    return render_template('template.html', my_string="Welcome to Python Flask Programming!", my_list=[0, 1, 2, 3, 4, 5])


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/student')
def student():
    return render_template('students/student.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        data = request.form
        return render_template("students/result.html", result=data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(port=5001, debug=True)
