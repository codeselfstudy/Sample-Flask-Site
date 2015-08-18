from flask import Blueprint, render_template, redirect, url_for, flash, jsonify

pages_bp = Blueprint('pages', __name__)

@pages_bp.route('/')
def index():
    data = {
        'title': 'Saluton, Mondo',
        'body': 'Bonvenon al mia retpagaro!'
    }
    return render_template('index.html', data=data)

@pages_bp.route('/page/<int:page_id>')
def pages(page_id):
    # Here you could do a database query to find the page with the ID of
    # `page_id`
    data = {}
    data['page_number'] = page_id
    data['type'] = 'page'
    data['message'] = 'You are viewing page #'
    return jsonify(data)

