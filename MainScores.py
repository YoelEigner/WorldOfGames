from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def score_server():
    score = open("./Scores.txt", 'r')
    return render_template('index.html', score=score.read())


@app.errorhandler(Exception)
def error(error):
    return render_template('error.html')


app.run(host="localhost", port=5001, debug=True)
