from flask import Flask

def register_blueprints(app_instance):
    from .views.pages import pages_bp
    from .views.wiki import wiki_bp
    app_instance.register_blueprint(pages_bp)
    app_instance.register_blueprint(wiki_bp)

app = Flask(__name__, instance_relative_config=True)

app.debug = True

register_blueprints(app)
