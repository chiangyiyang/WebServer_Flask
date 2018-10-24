from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    page = '''
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>This is a Heading</h1>
<p>This is a paragraph....</p>

</body>
</html>
  '''
    return page


app.run(
    host='0.0.0.0',   # 設定對外服務IP
    port=8080)        # 設定對外服務Port
