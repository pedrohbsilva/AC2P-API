from flask import jsonify, Blueprint, request
from app.models.User import User, UserSchema, user_share_schema, users_share_schema
from app.models.EvaluationDriver import EvaluationDriver, evaluationdriver_share_schema, evaluationsdrivers_share_schema, EvaluationDriverSchema
from app.models.EvaluationPassenger import EvaluationPassengers, evaluation_share_schema, EvaluationSchema, evaluations_share_schema
from app.models.Passenger import Passenger, PassengerSchema, passenger_share_schema, passengers_share_schema
from app.models.Driver import Driver, DriverSchema, driver_share_schema, drivers_share_schema
from app import app, db
from app.utils.authenticate import jwt_required
import jwt
EVALUATIONPASSENGER = Blueprint('evaluationPassenger', __name__,  url_prefix="/evaluationpassenger")

@EVALUATIONPASSENGER.route('/register', methods=['POST'])
def register():

  passenger_id = request.json['passenger_id']  
  driver_id = request.json['driver_id']  
  evaluation = request.json['evaluation']   

  evaluation_instace = EvaluationPassengers(
    passenger_id,
    driver_id,
    evaluation
  )  
  
  db.session.add(evaluation_instace)
  db.session.commit()
  
 

  return jsonify({"result": "sucesso"})

@EVALUATIONPASSENGER.route('/calculatedevaluationpassenger', methods=['GET'])
def index():

  passenger_id = request.args.get("passenger_id")
  driver_id = request.args.get("driver_id")
  
  test = evaluations_share_schema.dump(

    EvaluationPassengers.query.filter_by(passenger_id=passenger_id, driver_id=driver_id).all()

  )
  data = list()
  for x in test:
    data.append(x["evaluation"])
  totalaverage = 0
  finalaverage = 0
  for i in data:
    totalaverage += i
  
  finalaverage = totalaverage/len(data)
  print(finalaverage)

  return jsonify({"result": "#totalmedia"})