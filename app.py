from flask import Flask, request, render_template
import requests
import json
from urllib.request import urlopen
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    text = request.form['user_input']
    url = "https://"
    url1 = text
    url_final = url + url1
    page = urlopen(url_final)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    scrape = html
    json = {
        'text': scrape
    }
    headers = {
        "Content-Type": "application/json"
    }
    url = "https://hooks.slack.com/services/WEBHOOK_URL"

    response = requests.post(url,headers=headers,json=json)
    return render_template('index.html', scrape=scrape)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8080)
