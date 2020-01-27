from ecom import db


class SubCategory(db.Model):
    __tablename__ = 'subcategory'
    sub_category_id = db.Column(db.Integer(), primary_key=True)
    sub_category_name = db.Column(db.String(50))

    #Relationships
    pruduct=db.relationship('Product',backref='subcategory',lazy='joined',
                            cascade='all,delete')


    #FKs
    category_id=db.Column(db.Integer,db.ForeignKey('category.category_id'))