from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__, template_folder='template/html')

@app.route('/')
def home_page():
    user = {'username': 'Miguel'}
    return render_template('home.html', title='Home', user=user)

@app.route('/result')
def search_result():
    query = request.args.get('query')
    return render_template('result.html', title='Home', query=query)

if __name__ == '__main__':
    app.run()