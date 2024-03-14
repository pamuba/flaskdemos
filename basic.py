from flask import Flask, render_template, request
# from  flask.Request import request

app = Flask(__name__)

@app.route('/')
def index():
    name = "Flask",
    letter = list(name)
    dict = {'pup_name':'Sammy'}
    return render_template("basic.html",name = name,letter = letter)


@app.route('/information')
def info():
    return "<h1>Puppies are Cute</h1>"


@app.route('/thank_you')
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')
    # save to database
    return render_template('thankyou.html', first=first, last=last)


@app.route('/signup')
def signup_form():
    return render_template('basic.html')



if __name__ == '__main__':
    app.run(debug=True)