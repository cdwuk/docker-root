from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<marquee><h1>Congratulations you have succesfully built and are running Python code in a container</h1></marquee><iframe height='600' width='800' src='https://www.mancity.com/' />"

if __name__ == "__main__":
    app.run(host='0.0.0.0')


