from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from app.docs.combine_docs import combine_docs

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    
    db.init_app(app)
    
    from app.routes.item_routes import item_bp
    from app.routes.student_routes import student_bp
    app.register_blueprint(item_bp)
    app.register_blueprint(student_bp)
    
    @app.route('/')
    def index():
        return redirect(url_for('item.items'))
    
    @app.route('/info')
    def system_info():
        # Use combine_docs() to combine prompt.md and history files in reverse chronological order
        system_info_content = combine_docs()
        return render_template('system_info.html', system_info=system_info_content)
    
    return app