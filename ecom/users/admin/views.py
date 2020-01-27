from flask import Blueprint, jsonify, request,redirect,url_for,flash
import json
from ecom.classes.category import Category
from ecom.classes.sub_category import SubCategory
from ecom.classes.product import Product

from ecom import db

mod = Blueprint('admin', __name__, url_prefix='/admin')


@mod.route('/register', methods = ['POST'])
def admin_register():

    if request.method == 'POST':

        name = request.form['name']
        username=request.form['username']
        password=request.form['password']
        email = request.form['email']
        phone = request.form['phone']


        my_data = admin(name,username,password, email, phone)
        db.session.add(my_data)
        db.session.commit()

        flash("Admin Inserted Successfully")

        return redirect(url_for('Index'))

@mod.route('/login', methods=['POST'])
def login():
    request_data = request.form.to_dict()
    username = request_data['username']
    password = request_data['password']
    user = admin.query.filter(admin.username == username and admin.password == password).first()
    token = user.generate_auth_token()
    reponse = token
    return jsonify(reponse), 200
