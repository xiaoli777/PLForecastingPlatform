from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print("XIXI")
    strr = hello_1()
    return "Hello World!"

@app.route("/")
def hello_1():
    return "Hello World_1!"

if __name__ == "__main__":
    app.run()