from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello from a Python Standard</h1><img src='/app/images/cdw.png' /><img src='app/images/python.jpg' />"

if __name__ == "__main__":
    app.run(host='0.0.0.0')


