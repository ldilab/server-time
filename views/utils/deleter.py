import datetime

from models import db


def delete_before(model: db.Model, _at: datetime.datetime):
    db.session.query(model).filter(model.created_at < _at).delete()
    db.session.commit()
    return True
