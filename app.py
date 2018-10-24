from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'


app.run(
  host='0.0.0.0',   # 設定對外服務IP
  port=8080)        # 設定對外服務Port
