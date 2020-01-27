from flask import Blueprint, jsonify, request,redirect,url_for,flash

from ecom import db

mod = Blueprint('customer', __name__, url_prefix='/customer')

@mod.route('/register', methods = ['POST'])
def cus_register():

    if request.method == 'POST':

        name = request.form['name']
        username=request.form['username']
        password=request.form['password']
        email = request.form['email']
        phone = request.form['phone']
        address=request.form['address']
        bankac=request.form['banka/c']


        my_data = customer(name,username,password, email, phone,address,bankac)
        db.session.add(my_data)
        db.session.commit()

        flash("Customer Inserted Successfully")

        return redirect(url_for('Index'))

@mod.route('/login', methods=['POST'])
def login():
    request_data = request.form.to_dict()
    username = request_data['username']
    password = request_data['password']
    user = customer.query.filter(customer.username == username and customer.password == password).first()
    token = user.generate_auth_token()
    reponse = token
    return jsonify(reponse), 200

@mod.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = customer.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Customer Deleted Successfully")

    return redirect(url_for('Index'))

@mod.route('/update', methods = ['GET', 'POST'])
def update():

    if request.method == 'POST':
        c_data = customer.query.get(request.form.get('id'))

        c_data.name = request.form['name']
        c_data.username=request.form['username']
        c_data.password=request.form['password']
        c_data.email = request.form['email']
        c_data.phone = request.form['phone']
        c_data.address=request.form['address']
        c_data.bankac=request.form['banka/c']

        db.session.commit()
        flash("Customer Updated Successfully")

        return redirect(url_for('Index'))

