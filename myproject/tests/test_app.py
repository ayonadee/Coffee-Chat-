from flask import url_for
from flask_testing import TestCase
from application import db, app, models
from app import app
from datetime import datetime
# import the app's classes and objects

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///',
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # Create table
        
        db.create_all()

        # Create test network and users

       
        testuser = models.Users(first_name= "Ayona", last_name= "Duncan")
        db.session.add(testuser)
        year,month,day = map(int,"2020/09/21".split('/'))
        testnetwork = models.Network(first_name= "Ayonaa", last_name= "Duncan", email_address = "ayonaduncan@gmail.com", company = "Amazon", event = "Women in tech", spark = "We spoke about how we were both from West Africa and how she made the career switch from law to now working at a FAANG company", social_media_account= "ayoduncs on Twitter", contact_number = '123455678', meeting_date= datetime(year,month,day), position="consultant", user_id=models.Users.query.first().id)
        db.session.add(testnetwork)
        # save users and network to database
        db.session.commit()
        


    def tearDown(self):
        """
        Will be called after every test
        """
        db.session.remove()
        db.drop_all()
        # an_empty_string = ''
# Write a test class for testing that the home page loads but we are not able to run a get request for delete and update routes.
class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
       

    def test_network_get(self):
        response = self.client.get(url_for('network',user_id=1))
        self.assertEqual(response.status_code, 200)
        

    def test_contacts_get(self):
        response = self.client.get(url_for('contacts'))
        self.assertEqual(response.status_code, 200)
       

    def test_users_get(self):
        response = self.client.get(url_for('users'))
        self.assertEqual(response.status_code, 200)


# Test adding 
class TestAdd(TestBase):
    def test_add_post(self):
        year,month,day = map(int, "2020/09/21".split('/'))
        response = self.client.post(
            url_for('network',user_id=1),
            data = dict(first_name= "Ayonaa", last_name= "Duncan", email_address = "ayonaduncan@gmail.com", company = "Amazon", event = "Women in tech", spark = "We spoke about how we were both from West Africa and how she made the career switch from law to now working at a FAANG company", social_media_account= "ayoduncs on Twitter", contact_number= '123455678',meeting_date= datetime(year,month,day), position="consultant", user_id=1),
            follow_redirects=True
        )
        self.assertIn(b'Ayonaa',response.data)

    def test_add_post_users(self):
        response = self.client.post(
            url_for('users'),
            data = dict(first_name= "Ayona", last_name= "Duncan"),
            follow_redirects=True
        )
        self.assertIn(b'Ayona',response.data)


    def test_add_post_update(self):
        year,month,day = map(int, "2020/09/21".split('/'))
        response = self.client.post(
            url_for('update',id=1),
            data = dict(first_name= "Ayonaa", last_name= "Duncan", email_address = "ayonaduncan@gmail.com", company = "Amazon", event = "Women in tech", spark = "We spoke about how we were both from West Africa and how she made the career switch from law to now working at a FAANG company", social_media_account= "ayoduncs on Twitter", contact_number= '123455678',meeting_date= datetime(year,month,day), position="consultant", user_id=1),
            follow_redirects=True
        )
        self.assertIn(b'Ayonaa',response.data)

    def test_get_update(self):
        year, month, day = map(int,"2020/09/21".split('/'))
        response = self.client.get('update/1',follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Ayonaa',response.data)

    def test_post_nothing_users(self):
        response = self.client.post(
            url_for('users'),
            data = dict(first_name= "", last_name= ""),
            follow_redirects=True
        )
        self.assertIn(b'user does not exist',response.data)


    def test_post_nothing_network(self):
        year, month, day = map(int,"2020/09/21".split('/'))
        response = self.client.post(
            url_for('network',user_id=1),
            data = dict(first_name= "", last_name= "",email_address = "", company = "", event = "", spark = "", social_media_account= "", contact_number= "", meeting_date= datetime(year,month,day), position="", user_id=1),
            follow_redirects=True
        )
        self.assertIn(b'Please supply contact details for your network contact',response.data)

    def test_post_nothing_update(self):
        year, month, day = map(int,"2020/09/21".split('/'))
        response = self.client.post(
            url_for('update',id=1),
            data = dict(first_name= "", last_name= "",email_address = "", company = "", event = "", spark = "", social_media_account= "", contact_number= "", meeting_date= datetime(year,month,day), position="", user_id=1),
            follow_redirects=True
        )
        self.assertIn(b'No fields have been edited',response.data)


class Delete(TestBase):  
    def test_deleted(self):
        response = self.client.get('deletenetwork/1',follow_redirects= True)
        self.assertEqual(response.status_code, 200)
        assert b'Ayonaa' not in response.data