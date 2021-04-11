import json

from flask import session


class Serialize:
    def __init__(self):
        pass

    @staticmethod
    def serialize_json_session(instance, key: str):
        dt = {}
        dt.update(vars(instance))

        session[key] = json.dumps(dt, indent=4)

    @staticmethod
    def deserialize_json_session(cls, key: str):
        data = json.loads(session[key])

        this = object.__new__(cls)  # new class

        for k, value in data.items():
            setattr(this, k, value)

        return this
