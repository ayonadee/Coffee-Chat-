from application import app, db
from application.models import Users, Network

@app.route('/add')
def add():
    new_network = Network(first_name= "name of Contact",last_name = "last_name",email_address = "email_address", company = "company", position = "position in company",social_media_account = "social_media_account",contact_number = "contact_number",event = "event you met at",spark = " things discussed that you bonded over or remember",date = "date you met", user_id = "user_id")
    db.session.add(new_network)
    db.session.commit()
    return "Added new network contact to database"

@app.route('/add/user')
def add_user():
    new_user = Users(first_name = "name", last_name ="last name")
    db.session.add(new_user)
    db.session.commit()

@app.route('/read')
def read():
    all_networks = Network.query.all()
    network_string = ""
    for network in all_networks:
        network_string += "<br>"+ network.first_name
    return network_string

@app.route('/update/<first_name>')
def update(first_name):
    first_network = Network.query.first()
    first_network.first_name = first_name
    db.session.commit()
    return first_network.first_name

@app.route('/delete')
def delete():
    network_to_delete = Network.query.first()
    db.session.delete(network_to_delete)
    db.session.commit()
    return 'You have deleted an entry'
