import json

from flask import session


class Serialize:
    def __init__(self):
        pass

    @staticmethod
    def serialize_json_session(instance, key: str):
        dt = {}
        dt.update(vars(instance))

        session[key] = dt

    @staticmethod
    def deserialize_json__session(cls, key: str):
        data = json.loads(session[key])

        instance = object.__new__(cls)

        for key, value in data.items():
            setattr(instance, key, value)

        return instance
