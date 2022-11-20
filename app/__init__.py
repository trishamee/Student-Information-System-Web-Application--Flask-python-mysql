from flask import Flask,render_template
from flask_mysql_connector import MySQL
from flask_bootstrap import Bootstrap
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY, BOOTSTRAP_SERVE_LOCAL, CLOUD_NAME, API_KEY, API_SECRET
from flask_wtf.csrf import CSRFProtect
import cloudinary

mysql = MySQL()
bootstrap = Bootstrap()

# set up 
def create_app(test_config=None):
    app = Flask(__name__, template_folder='html-template', instance_relative_config=True)
    
    #error handling -- 404
    @app.errorhandler(404)
    def not_found(e):
    # note that we set the 404 status explicitly
        return render_template('error-404.html'), 404

    cloudinary.config(
        CLOUD_NAME = CLOUD_NAME,
        API_KEY = API_KEY,
        API_SECRET = API_SECRET
    )

    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        MYSQL_USER=DB_USERNAME,
        MYSQL_PASSWORD=DB_PASSWORD,
        MYSQL_DATABASE=DB_NAME,
        MYSQL_HOST=DB_HOST,
        BOOTSTRAP_SERVE_LOCAL=BOOTSTRAP_SERVE_LOCAL
    )

    bootstrap.init_app(app)
    mysql.init_app(app)
    CSRFProtect(app)

    from .routes import routes
    app.register_blueprint(routes, url_prefix='/')

    return app