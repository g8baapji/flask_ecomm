from ecom import db


class Category(db.Model):
    __tablename__ = 'category'
    category_id = db.Column('category_id', db.Integer(), primary_key=True)
    category_name = db.Column('category_name', db.String(50))

    #Relationships
    subcategory= db.relationship('SubCategory', backref='category',
                                 lazy='joined',cascade="all,delete")

    #FKs




    def __repr__(self):
        return f"Cat({self.category_id},{self.category_name})"