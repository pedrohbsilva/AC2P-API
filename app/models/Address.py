from app import db, ma
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.Driver import Driver
from app.models.Passenger import Passenger

class Address(db.Model):
  __tablename__ = 'addresses'
  id = db.Column(db.Integer, autoincrement=True, primary_key=True)
  passenger_id = db.Column(db.Integer, db.ForeignKey(Passenger.id), nullable=False)
  driver_id = db.Column(db.Integer, db.ForeignKey(Driver.id), nullable=False)
  address_start = db.Column(db.String(84), nullable=False)
  address_end = db.Column(db.String(84), nullable=False)
  time_start = db.Column(db.DateTime, nullable=False)
  time_end = db.Column(db.DateTime, nullable=False)
  
  def __init__(self, passenger_id, driver_id, address_start, address_end, time_start, time_end):
    self.passenger_id = passenger_id
    self.driver_id = driver_id
    self.address_start = address_start
    self.address_end = address_end
    self.time_start = time_start
    self.time_end = time_end

class AddressSchema(ma.Schema):
  class Meta:
    fields = ('id', 
              'passenger_id', 
              'driver_id', 
              'address_start', 
              'address_end', 
              'time_start', 
              'time_end')
    
address_share_schema = AddressSchema()
addresses_share_schema = AddressSchema(many=True)