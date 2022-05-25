from email import message
from flask import Flask, render_template, request

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/testdb'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if(request.method == 'POST'):
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        # print(f"I {customer} puchased a Lexus vehicle and I would like to give a rating of {rating} to {dealer} with a feedback: {comments}")
        if customer == "" or dealer == "":
            return render_template('index.html', message="Please entered the required fields")
        return render_template('success.html')

if __name__ == "__main__":
    app.run()