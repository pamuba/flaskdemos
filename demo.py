from flask import Flask

app = Flask(__name__)

# 127.0.0.1:5000
@app.route('/')
def index():
    return "<h1>Hello Flask!!</h1>"

@app.route('/information')
def info():
    return "<h1>Puppies are Cute</h1>"


@app.route('/puppy/<name>/<breed>')
def puppy(name, breed):
    return "<h1>{} Puppies are Cute</h1>".format(breed.upper())


@app.route('/calc/<num>')
def calc(num):
    return "<h1>{} Puppies are Cute</h1>".format(num * 2)


if __name__ == '__main__':
    app.run(debug=True)