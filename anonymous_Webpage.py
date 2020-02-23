from flask import Flask, request
from twitter_bot import *

app = Flask(__name__)
import nltk
nltk.download('vader_lexicon')

api = create_api()


@app.route("/")
def hello():
    return '<form action="/echo" method="POST"><input style="height:400px; width:600px" name="text" placeholder="Enter your content anonymously"><br><br><input type="submit" value="Submit"></form>'


@app.route("/echo", methods=['POST'])
def echo():
    with open("content.txt","w") as content_file:
        content = request.form['text']
        content_file.write(content)
    content_file.close()
    api.update_status(content)
    return "You said: " + content


if __name__ == "__main__":
    app.run(host="10.219.134.189",port="8000")



