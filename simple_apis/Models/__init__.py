from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


class User(db.Model):
      id=db.Column(db.Integer, primary_key=True)
      username=db.Column(db.String(50), unique=True, nullable=False)
      email=db.Column(db.String(50), unique=True, nullable=False)
      password=db.Column(db.String(100), nullable=False)
      created_at=db.Column(db.DateTime,  server_default=func.now())

      def __repr__(self):
            return f'User {self.username}'

#user's Marshmallow Schema
class UserSchema(ma.SQLAlchemySchema):
     class Meta:
           model=User
           fields=("username", "email", "password")

user_schema=UserSchema()
users_schema=UserSchema(many=True)