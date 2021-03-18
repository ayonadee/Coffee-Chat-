from application import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=True)
    last_name = db.Column(db.String(30), nullable=True)
    network = db.relationship('Network', backref='network') 

class Network(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=True)
    last_name = db.Column(db.String(30), nullable=True)
    email_address = db.Column(db.String(50),nullable=True)
    company = db.Column(db.String(60), nullable=True)
    position = db.Column(db.String(60), nullable=True)
    social_media_account = db.Column(db.String(400), nullable=True)
    contact_number = db.Column(db.String(30), nullable=True)
    event = db.Column(db.String(80), nullable=True)
    meeting_date = db.Column(db.DateTime, nullable=True)
    spark = db.Column(db.String(9000), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)