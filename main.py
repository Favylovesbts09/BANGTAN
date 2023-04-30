from flask import flask 
app = Flask (__name__)
@app.route("/")
def hello():
  return "Hello! This is a basic Flask app. "
if __name__ == "_main_" :
    app.run("0.0.0.0")
