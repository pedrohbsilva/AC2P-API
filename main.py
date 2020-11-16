from flask import jsonify

from app import app, db, manager, api
from app.models.User import User
from app.models.Passenger import Passenger
from app.models.Driver import Driver
from app.models.Evaluation import Evaluation
from app.controllers.user_controller import USER

app.register_blueprint(USER)

@app.route('/')
def index():
  return "Servidor da AC2P Ligado!"
      
if __name__ == "__main__":
  manager.run()
