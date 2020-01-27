from flask import Blueprint, jsonify, request,redirect,url_for,flash

from ecom import db

mod = Blueprint('admin', __name__, url_prefix='/vendor')


@mod.route('/register', methods = ['POST'])
def vendor_register():
    if request.method == 'POST':

        name = request.form['name']
        uname=request.form['uname']
        password=request.form['password']
        email = request.form['email']
        phone = request.form['phone']
        company = request.form['company']
        address= request.form['address']
        bankac= request.form['bank_a/c']

        my_data = vendor(name,uname,password, email, phone,company,address,bankac)
        db.session.add(my_data)
        db.session.commit()

        flash("vander Inserted Successfully")

        return redirect(url_for('Index'))
