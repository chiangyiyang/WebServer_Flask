from flask import Flask
from flask import render_template, request
import json

app = Flask(__name__, static_folder='static')


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


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print("POST: " + request.form['username'])
        return "HELLO " + request.form['username']
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


@app.route('/dht', methods=['POST'])
def getDht():
    if request.method == 'POST':
        msg = "POST: " + json.dumps(request.json)
        data = request.json
        f = open('log.txt', 'a')
        f.write(str(data['temperature']) + ', ' + str(data['humidity']) + '\n')
        f.close()
        return msg


@app.route('/dht_log')
def getDhtLog():
    f = open('log.txt', 'r')
    data = f.read()
    f.close()
    return data.replace('\n', '<br>')


@app.route('/chart_t')
def getTemperatureChart():
    f = open('log.txt', 'r')
    data = f.read()
    f.close()
    data = ', '.join([l.split(',')[0] for l in data.split('\n')])
    return render_template('chart.html', title='Temperature', data=data)


app.run(
    host='0.0.0.0',   # 設定對外服務IP
    port=8080)        # 設定對外服務Port
