from flask import Flask
from flask import render_template
from flask import request

from main import searchTopic

app = Flask(__name__, template_folder='template/html')


@app.route('/')
def home_page():
    return render_template('home.html', title='Home')


@app.route('/result')
def search_result():
    query = request.args.get('query')
    results = searchTopic(query)
    return render_template('result.html', title='Home', query=results)


if __name__ == '__main__':
    app.run()
