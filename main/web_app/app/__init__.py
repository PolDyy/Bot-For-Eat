from flask import Flask
import os, config

# создание экземпляра приложения
app = Flask(__name__)
app.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopementConfig')

# инициализирует расширения
# db = SQLAlchemy(app)
# mail = Mail(app)
# migrate = Migrate(app, db)
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'

from . import views
