from app import db, ma
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.User import User

class Driver(db.Model):
  __tablename__ = 'drivers'
  id = db.Column(db.Integer, autoincrement=True, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
  car = db.Column(db.String(84), nullable=False)
  car_plate = db.Column(db.String(84), nullable=False)
  cnh = db.Column(db.String(84), nullable=False, unique=True)

  def __init__(self, user_id, car, car_plate, cnh):
    self.user_id = user_id
    self.car = car
    self.car_plate = car_plate
    self.cnh = cnh

class DriverSchema(ma.Schema):
  class Meta:
    fields = ('id', 'user_id','car','car_plate','cnh' )
    
driver_share_schema = DriverSchema()
drivers_share_schema = DriverSchema(many=True)