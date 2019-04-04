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
    print(query)
    results = searchTopic(query)
    print(results)
    return render_template('result.html', title='Home', results=results)


if __name__ == '__main__':
    app.run()
