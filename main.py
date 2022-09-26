from flask import Flask, render_template, redirect, url_for, request, flash
import requests
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(20)

@app.route('/', methods=['GET', 'POST'])
def index():
    url = "https://api.apilayer.com/short_url/hash"
    headers = {
        "apikey": "4WHDlrjPgAxHDAY5MlOapFEehZBJDqto"
    }
    if request.method == 'POST':
        long_url = request.form.get('long_url')
        if not long_url:
            flash(message='Please insert a URL!!!')
            return redirect(request.url)
        response = requests.request("POST", url, headers=headers, data=long_url)
        status_code = response.status_code
        if status_code != 200:
            flash('API status code error')
            return redirect(request.url)
        result = response.json()['short_url']
        return render_template('index.html', short_url=result)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
