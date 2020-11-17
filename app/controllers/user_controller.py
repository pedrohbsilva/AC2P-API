from flask import jsonify, Blueprint, request
from app.models.User import User, UserSchema, user_share_schema, users_share_schema
from app.models.Passenger import Passenger, PassengerSchema, passenger_share_schema, passengers_share_schema
from app.models.Driver import Driver, DriverSchema, driver_share_schema, drivers_share_schema
from app import app, db
from app.utils.authenticate import jwt_required
import jwt
USER = Blueprint('user', __name__,  url_prefix="/user")
  
@USER.route('/register', methods=['POST'])
def register():

  name = request.json['name']  
  cpf = request.json['cpf']   
  email = request.json['email']
  phone = request.json['phone']
  password = request.json['password']
  type_user = request.json['type_user']
  
  user = User(
    name,
    email,
    cpf,
    phone,
    password
  )  
  
  db.session.add(user)
  db.session.commit()
  
  resultUser = user_share_schema.dump(
    User.query.filter_by(email=email).first()
  )
  
  if type_user == 1:
    passenger = Passenger(
      resultUser['id'],
    )
    db.session.add(passenger)
    db.session.commit()
    
  if type_user == 2:
    car = request.json['car']   
    car_plate = request.json['car_plate']
    cnh = request.json['cnh']
  
    driver = Driver(
      resultUser['id'],
      car,
      car_plate,
      cnh
    )
    db.session.add(driver)
    db.session.commit()

  return jsonify(resultUser)
  
@USER.route('/login', methods=['POST'])
def login():
  email = request.json['email']
  password = request.json['password']
  
  user = User.query.filter_by(email=email).first_or_404()
  
  if not user.verify_password(password):
    return jsonify({
      "error": "Suas informações estão incorretas"
    }), 403
  
  payload = {
    "id": user.id,
  }
  
  token = jwt.encode(payload, app.config['SECRET_KEY'])
  
  return jsonify({"token": token.decode('utf-8')})

@USER.route('/protected', methods=['GET'])
@jwt_required 
def index(current_user):
  result = users_share_schema.dump(
    User.query.all()
  )
  
  return jsonify(result)