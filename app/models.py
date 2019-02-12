from . import db

# Creating user

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):

    __tablename__ = 'pitch'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(255))
    #author_id =db.Column(db.Integer, db.Foreignkey('users.id'))
   
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
    def __repr__(self):
        return f'Pitch {self.content}'
