from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello from a Python Standard</h1><img alt='cdw.png' title='cdw.png' src='images1/cdw.png' /><img alt='python.jpg' title='python.jpg' src='images/python.jpg' />"

if __name__ == "__main__":
    app.run(host='0.0.0.0')


