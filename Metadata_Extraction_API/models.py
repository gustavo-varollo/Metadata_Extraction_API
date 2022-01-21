from . import db


class Metadata(db.Model):
    """
    Class model that creates the database and its tables
    """
    __tablename__ = 'files_metadata'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    key = db.Column(
        db.String(64),
        index=False,
        unique=True,
        nullable=False
    )
    name = db.Column(
        db.String(64),
        index=False,
        unique=True,
        nullable=False
    )
    path = db.Column(
        db.String(80),
        index=True,
        unique=True,
        nullable=False
    )
    created = db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=False
    )
    modified = db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=True
    )
    mime_type = db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=True
    )
    extension = db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=True
    )

    def __repr__(self):
        return '<File Name {}>'.format(self.name)
