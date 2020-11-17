from app import db, ma
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.User import User
from app.models.Payment import Payment

class PaymentUser(db.Model):
  __tablename__ = 'payment_users'
  id = db.Column(db.Integer, autoincrement=True, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
  payment_id = db.Column(db.Integer, db.ForeignKey(Payment.id), nullable=False)
  price = db.Column(db.Integer, nullable=False)
  
  def __init__(self, user_id, payment_id, price):
    self.user_id = user_id
    self.payment_id = payment_id
    self.price = price

class PaymentUserSchema(ma.Schema):
  class Meta:
    fields = ('id', 'user_id', 'payment_id', 'price')
    
payment_user_share_schema = PaymentUserSchema()
payment_users_share_schema = PaymentUserSchema(many=True)