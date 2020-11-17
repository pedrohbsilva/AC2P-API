from flask import jsonify

from app import app, db, manager, api
from app.controllers.user_controller import USER
from app.models.Address import Address
from app.models.Driver import Driver
from app.models.Evaluation import Evaluation
from app.models.Passenger import Passenger
from app.models.Payment import Payment
from app.models.PaymentUser import PaymentUser
from app.models.User import User

app.register_blueprint(USER)

@app.route('/')
def index():
  return "Servidor da AC2P Ligado!"
      
if __name__ == "__main__":
  manager.run()
