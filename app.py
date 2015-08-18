from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        'title': 'Saluton, Mondo',
        'body': 'Bonvenon al mia retpagaro!'
    }
    return render_template('index.html', data=data)

@app.route('/page/<int:page_id>')
def pages(page_id):
    # Here you could do a database query to find the page with the ID of
    # `page_id`
    data = {}
    data['page_number'] = page_id
    data['type'] = 'page'
    data['message'] = 'You are viewing page #'
    return jsonify(data)

@app.route('/wiki/Virtualenv')
def virtualenv_whatever_you_want():
    return 'This is a page about Virtualenvs!!!'

if __name__ == '__main__':
    app.run(debug=True)
