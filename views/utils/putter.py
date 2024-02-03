from typing import Any, Dict

from models import db


def put_value(model: db.Model, values: Dict[str, Any]):
    new_value = model(**values)
    db.session.add(new_value)
    db.session.commit()
    return new_value
