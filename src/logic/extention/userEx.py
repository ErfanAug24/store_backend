from flask_jwt_extended import current_user


class Current_user:
    @classmethod
    def is_authenticated(cls):
        return True if current_user else False

    @classmethod
    def get_current_authenticated_user(cls):
        return current_user if current_user else False
