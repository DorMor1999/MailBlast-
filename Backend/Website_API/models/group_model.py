from app import db

class Group(db.Model):
    __tablename__ = 'groups'  # Name of the table in the database
    group_id = db.Column(db.Integer, primary_key=True)
    group_admin_id = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    group_name = db.Column(db.String(120), nullable=False)
    group_description = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.Date, nullable=False)

     # Relationship to the User model (for the group admin)
    group_admin = db.relationship('User', backref='admin_groups', lazy=True)

    # Relationship to the Customer model through the group_customer association table
    customers = db.relationship('Customer', backref='group', lazy=True)

    def __repr__(self):
        return (f"<Group group_id={self.group_id}, "
                f"group_admin_id={self.group_admin_id}, "
                f"group_name='{self.group_name}', "
                f"group_description='{self.group_description}', "
                f"created_at={self.created_at}>")

    def to_dict(self):
        return {
            'group_id': self.group_id,
            'group_admin_id': self.group_admin_id,
            'group_name': self.group_name,
            'group_description': self.group_description,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }