from app import db, ma
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.User import User
from sqlalchemy.sql import table, column

class Payment(db.Model):
  __tablename__ = 'payments'
  id = db.Column(db.Integer, autoincrement=True, primary_key=True)
  description = db.Column(db.String(84), nullable=False)

  def __init__(self, description):
    self.description = description
  

  @classmethod
  def seed(x, payments_methods):
    for description_payment in payments_methods:
      payment = Payment(
          description = description_payment,
      )
      payment.save()
    
  def save(self):
      db.session.add(self)
      db.session.commit()
        
class PaymentSchema(ma.Schema):
  class Meta:
    fields = ('id', 'description' )

payment_share_schema =  PaymentSchema()
payments_share_schema =  PaymentSchema(many=True)

payments_methods = ['Cartão de débito', 'Cartão de Crédito', 'Dinheiro']

populate = False

if populate == True: 
  Payment.seed(payments_methods)
