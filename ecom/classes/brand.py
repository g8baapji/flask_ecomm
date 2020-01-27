from ecom import db


class Brand(db.Model):
    __tablename__ = 'brand'
    brand_id = db.Column(db.Integer(), primary_key=True)
    brand_name = db.Column(db.String(50))

    # Relationships
    product = db.relationship('Product', backref='brand', lazy='joined',
                              cascade='all,delete')

    # FKs

    def __repr__(self):
        return f"Brand({self.brand_name})"
