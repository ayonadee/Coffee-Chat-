from app import db
from application import models 


db.drop_all()
db.create_all()

testuser = models.Users(first_name= "Ayona", last_name= "Duncan")
db.session.add(testuser)
db.session.commit()

testnetwork = models.Network(first_name= "Ayonaa", last_name= "Duncan", email_address = "ayonaduncan@gmail.com", company = "Amazon", event = "Women in tech", spark = "We spoke about how we were both from West Africa and how she made the career switch from law to now working at a FAANG company", social_media_account= "ayoduncs on Twitter", date= "2020-04-09", position="consultant", user_id=1)
db.session.add(testnetwork)
db.session.commit()