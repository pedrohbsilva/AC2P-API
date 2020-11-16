from app import db, ma
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.User import User

class Passenger(db.Model):
  __tablename__ = 'passengers'
  id = db.Column(db.Integer, autoincrement=True, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

  def __init__(self, user_id):
    self.user_id = user_id

class PassengerSchema(ma.Schema):
  class Meta:
    fields = ('id', 'user_id' )
    
passenger_share_schema = PassengerSchema()
passengers_share_schema = PassengerSchema(many=True)