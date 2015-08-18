from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Saluton, Mondo!'

@app.route('/page/<int:page_id>')
def pages(page_id):
    # Here you could do a database query to find the page with the ID of
    # `page_id`
    return 'You are viewing page #{}'.format(page_id)

@app.route('/wiki/Virtualenv')
def virtualenv_whatever_you_want():
    return 'This is a page about Virtualenvs!!!'

if __name__ == '__main__':
    app.run(debug=True)
