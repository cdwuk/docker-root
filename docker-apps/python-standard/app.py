from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<div style='font-size:30pt;background-color:lightyellow'>Hello from a Python Script running in a Linux container!<div>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')


