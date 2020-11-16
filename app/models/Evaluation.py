from app import db, ma
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.User import User

class Evaluation(db.Model):
  __tablename__ = 'Evaluations'
  id = db.Column(db.Integer, autoincrement=True, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
  evaluation = db.Column(db.Integer, nullable=False)

  def __init__(self, user_id, evaluation):
    self.user_id = user_id
    self.evaluation = evaluation

class EvaluationSchema(ma.Schema):
  class Meta:
    fields = ('id', 'user_id', 'evaluation' )

evaluation_share_schema = EvaluationSchema()
evaluations_share_schema = EvaluationSchema(many=True)