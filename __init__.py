from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app,db)

from helloapp import routes

## Write the required code below which runs flask applictaion 'app' defined above
## on host 0.0.0.0 and port 8000    
if __name__=='__main__':
	app.run(host='127.0.0.1',port=8010)
