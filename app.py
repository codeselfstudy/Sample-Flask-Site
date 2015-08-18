from flask import Flask

app = Flask(__name__)

@app.routes('/wiki/Virtualenv')
def virtualenv_whatever_you_want():
    return 'This is a page about Virtualenvs!!!'

if __name__ == '__main__':
    app.run(debug=True)
