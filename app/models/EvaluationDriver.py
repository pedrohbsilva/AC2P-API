from app import db, ma
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.User import User
from app.models.Passenger import Passenger
from app.models.Driver import Driver

class EvaluationDriver(db.Model):
  __tablename__ = 'evaluationdrivers'
  id = db.Column(db.Integer, autoincrement=True, primary_key=True)
  passenger_id = db.Column(db.Integer, db.ForeignKey(Passenger.id), nullable=False)
  driver_id = db.Column(db.Integer, db.ForeignKey(Driver.id), nullable=False)
  evaluation = db.Column(db.Integer, nullable=False)

  def __init__(self, passenger_id, driver_id, evaluation):
    self.passenger_id = passenger_id
    self.driver_id = driver_id
    self.evaluation = evaluation

class EvaluationDriverSchema(ma.Schema):
  class Meta:
    fields = ('id', 'passenger_id', 'driver_id', 'evaluation' )

evaluationdriver_share_schema = EvaluationDriverSchema()
evaluationsdrivers_share_schema = EvaluationDriverSchema(many=True)