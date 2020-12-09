from flask import jsonify

from app import app, db, manager
from app.controllers.user_controller import USER
from app.controllers.evaluationDriver_controller import EVALUATIONDRIVER
from app.controllers.evaluationPassenger_controller import EVALUATIONPASSENGER
from app.models.Address import Address
from app.models.Driver import Driver
from app.models.EvaluationDriver import EvaluationDriver
from app.models.EvaluationPassenger import EvaluationPassengers
from app.models.Passenger import Passenger
from app.models.Payment import Payment
from app.models.PaymentUser import PaymentUser
from app.models.User import User

app.register_blueprint(USER)
app.register_blueprint(EVALUATIONPASSENGER)
app.register_blueprint(EVALUATIONDRIVER)

@app.route('/')
def index():
  return "Servidor da AC2P Ligado!"
      
if __name__ == "__main__":
  manager.run()
