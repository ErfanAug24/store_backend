def error_structure(message, status_code):
    return {"error": {"message": message,
                      "status_code": status_code}}, status_code


USER_CONFLICT = error_structure(
    "User with this username is already exist.", 409)
USER_NOT_FOUND = error_structure(
    "User with this is not exist in database.", 404)
PERMISSION = error_structure(
    "Invalid credentials.", 401)
UNKNOWN_ERROR = error_structure(
    "An Unknown error happend.", 0)
SOMETHING_WENT_WRONG = error_structure(
    "Please try Again Later . Something went wrong.", 500)


class Error_Syntaxts(Exception):
    def __init__(self, message, status_code=None, *args: object) -> None:
        Exception.__init__(self, *args)
        self.message = message
        self.status_code = status_code

    def detective(cls):
        _errors = {409: cls.user_conflict,
                   404: cls.user_not_found,
                   401: cls.permission_required,
                   500: cls.something_went_wrong
                   }
        _custom_error = {
            cls.status_code: error_structure(cls.message, cls.status_code)
        }
        error_func = _errors.get(cls.status_code)

        if not error_func:
            return _custom_error.get(cls.status_code)

        return error_func()

    @ classmethod
    def user_conflict(cls):
        return USER_CONFLICT

    @ classmethod
    def user_not_found(cls):
        return USER_NOT_FOUND

    @ classmethod
    def permission_required(cls):
        return PERMISSION

    @ classmethod
    def something_went_wrong(cls):
        return SOMETHING_WENT_WRONG

    @ classmethod
    def unknown_error(cls):
        return UNKNOWN_ERROR
