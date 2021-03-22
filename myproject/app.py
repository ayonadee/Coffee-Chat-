from application import app, models, db
from flask import Flask, render_template,request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField, DateTimeField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lockedout'


class UserForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    submit = SubmitField('Submit New User')

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
    meeting_date = DateTimeField('Date')
    user_id = IntegerField('user id')
    submit = SubmitField('Submit New Contact')
    

@app.route('/network/<int:user_id>', methods=['GET','POST'])
def network(user_id):
    error=""
    form = NetworkForm()
    form.user_id.data = user_id
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
        meeting_date = form.meeting_date.data
        user_id = user_id

        if len(first_name) == 0 or len(last_name) == 0 or len(email_address) == 0 or len(company) == 0 or len(position) == 0 or len(social_media_account) == 0 or len(contact_number) == 0  or len(event) == 0 or len(spark) == 0 or len(str(meeting_date)) == 0:
            error = "Please supply contact details for your network contact"
        else:
            new_contact = models.Network(first_name = form.first_name.data,
            last_name = form.last_name.data,email_address = form.email_address.data, 
            company = form.company.data, position = form.position.data,
            social_media_account = form.social_media_account.data,contact_number = form.contact_number.data,
            event = form.event.data,spark = form.spark.data,meeting_date = form.meeting_date.data , user_id = user_id)
            db.session.add(new_contact)
            db.session.commit()
            return redirect('/contacts')
    users = models.Users.query.all()
    return render_template('network.html', form=form, users=users, message=error)

@app.route('/home', methods = ['GET', 'POST'])
@app.route('/',methods = ['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/users', methods =['GET','POST'])
def users():
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
            return redirect('/users')
    users = models.Users.query.all()
    return render_template('users.html',form=form, users=users, message=error)
            
@app.route('/contacts')
def contacts():
    networks = models.Network.query.all()
    return render_template('contacts.html', networks=networks)

@app.route('/deletenetwork/<int:id>')
def delete(id):
    network_to_delete = models.Network.query.filter_by(id=id).first()
    db.session.delete(network_to_delete)
    db.session.commit()
    return redirect('/contacts')


@app.route('/update/<int:id>', methods =['POST', 'GET'])
def update(id):
    first_network = models.Network.query.filter_by(id=id).first()
    error=""
    form = NetworkForm()
    form.user_id.data = id
    
    if(request.method=='POST'):
        first_network.first_name = form.first_name.data
        first_network.last_name= form.last_name.data
        first_network.email_address = form.email_address.data
        first_network.company = form.company.data
        first_network.position = form.position.data
        first_network.social_media_account = form.social_media_account.data
        first_network.contact_number = form.contact_number.data
        first_network.event = form.event.data
        first_network.spark = form.spark.data
        first_network.meeting_date = form.meeting_date.data
        
        if len(form.first_name.data) == 0 or len(form.last_name.data) == 0 or len(form.email_address.data) == 0 or len(form.company.data) == 0 or len(form.position.data) == 0 or len(form.social_media_account.data) == 0 or len(form.contact_number.data) == 0  or len(form.event.data) == 0 or len(form.spark.data) == 0 or len(str(form.meeting_date.data)) == 0:
            error = "No fields have been edited"
        else:
            db.session.commit()
            return redirect('/contacts')
    else:
        form.first_name.data = first_network.first_name
        form.last_name.data = first_network.last_name
        form.email_address.data = first_network.email_address
        form.company.data = first_network.company
        form.position.data = first_network.position
        form.social_media_account.data = first_network.social_media_account
        form.contact_number.data = first_network.contact_number
        form.event.data = first_network.event
        form.spark.data = first_network.spark
        form.meeting_date.data = first_network.meeting_date
        return render_template('network.html', form=form, users=users, message1=error) 
   

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')