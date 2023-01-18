import os
import logging
from flask_cors import CORS

from project import app

app.debug = True
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# logging.getLogger('flask_cors').level = logging.DEBUG
logging.basicConfig(level=logging.DEBUG)