from flask import Blueprint, render_template, redirect, url_for, flash, jsonify

wiki_bp = Blueprint('wiki', __name__)

@wiki_bp.route('/wiki/Virtualenv')
def virtualenv_whatever_you_want():
    data = {
        'title': 'About Virtualenvs',
        'body': 'This is a page about Virtualenvs!!!'
    }
    return render_template('wiki/virtualenv.html', data=data)
