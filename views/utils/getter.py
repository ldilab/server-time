from sqlalchemy import func

from models import db


def get_average_in(model: db.Model, _in: str):
    if _in not in ["h", "d", "w", "m"]:
        raise ValueError("_in must be 'h', 'd', 'w', or 'm'")

    last_time = model.query.order_by(model.created_at.desc()).first().created_at
    delta_time = {
        'h': func.hour(1),
        'd': func.day(1),
        'w': func.week(1),
        'm': func.month(1),
    }
    return db.session.query(func.avg(model.value)).filter(model.created_at > last_time - delta_time.get(_in)).scalar()
