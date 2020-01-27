from ecom import db
from ecom.classes.brand import Brand


class Product(db.Model):
    __tablename__ = 'product'
    product_id = db.Column(db.Integer(), primary_key=True)
    product_name = db.Column(db.String(50))

    #Relationships


    #FKs
    sub_category_id=db.Column(db.Integer,db.ForeignKey('subcategory.sub_category_id'))
    brand_id=db.Column(db.Integer,db.ForeignKey('brand.brand_id'))