from application import app, models, db, routes
from flask import Flask, render_template,request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lockedout'


class UserForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')

class NetworkForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email_address = StringField('Email Address')
    company = StringField('Company')
    position = StringField('Position')
    social_media_account = StringField('Social Media')
    contact_number = StringField('Contact Number')
    event = StringField('Event')
    spark = StringField('Spark')
    date = DateField('Date')
    user_id = IntegerField('user id')
    submit = SubmitField('Submit New Contact')
    

@app.route('/network', methods=['GET','POST'])
def network():
    error=""
    form = NetworkForm()
    
    if(request.method=='POST'):
        first_name = form.first_name.data
        last_name = form.last_name.data
        email_address = form.email_address.data
        company = form.company.data
        position = form.position.data
        social_media_account = form.social_media_account.data
        contact_number = form.contact_number.data
        event = form.event.data
        spark = form.spark.data
        date = form.date.data
        user_id = form.user_id.data
    
        if len(first_name) == 0 or len(last_name) == 0 or len(email_address) == 0 or len(company) == 0 or len(position) == 0 or len(social_media_account) == 0 or len(contact_number) == 0  or len(event) == 0 or len(spark) == 0 or len(str(date)) == 0:
            error = "Please supply contact details for your network contact"
        else:
            new_contact = models.Network(first_name = form.first_name.data,
            last_name = form.last_name.data,email_address = form.email_address.data, 
            company = form.company.data, position = form.position.data,
            social_media_account = form.social_media_account.data,contact_number = form.contact_number.data,
            event = form.event.data,spark = form.spark.data,date = form.date.data, user_id = form.user_id.data)
            db.session.add(new_contact)
            db.session.commit()
            return redirect('/contacts')
    return render_template('network.html', form=form, message=error)



@app.route('/home', methods =['GET','POST'])
@app.route('/', methods=['GET','POST'])
def home():
    error=""
    form = UserForm()
    if(request.method=='POST'):
        first_name = form.first_name.data
        last_name = form.last_name.data
        if len(first_name) == 0 or len(last_name) == 0:
            error = 'user does not exist'
        else:
            new_user = models.Users(first_name = form.first_name.data, last_name =form.last_name.data)
            db.session.add(new_user)
            db.session.commit()
            return 'welcome to Coffee chat'
            return redirect('/contacts')
    return render_template('home.html',form=form,message=error)
            
@app.route('/contacts', methods=['GET','POST'])
def contacts():
    networks = models.Network.query.all()
    return render_template('contacts.html', networks=networks)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')