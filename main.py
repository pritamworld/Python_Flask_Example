from flask import Flask, request, render_template

app = Flask(__name__)
print(__name__)


# http://127.0.0.1:5001/
@app.route("/", methods=["GET"])
def hello():
    return "<h1>Welcome to Python Flask Example</h1>"


# http://127.0.0.1:5001/hello
@app.route("/hello", methods=["GET"])
def greet():
    return "<h1>Hello World</h1>"


# http://127.0.0.1:5001/name
# This should return your name
@app.route("/name", methods=["GET"])
def name():
    print(request)
    return "<h1>Pritesh Patel</h1>"


# path parameter example
# http://127.0.0.1:5001/hello/pritesh/lambton
@app.route('/hello/<user>/<org>')
def hello_name(user, org):
    return render_template('hello.html', name=user, org=org)


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
