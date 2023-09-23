def message_structure(message, status_code):
    return {"error": {"message": message,
                      "status_code": status_code}}, status_code


USER_CREATION = message_structure(
    "User was created Successfully.", 201)
USER_DELETE = message_structure(
    "The user is deleted.", 200)
USER_UPDATE = message_structure(
    "The user is successfully updated.", 200)
USER_LOGIN = message_structure(
    "The user is successfully logged in.", 200)
USER_LOGOUT = message_structure(
    "The user is successfully logged out.", 200)
TYPE_PASSWORD = message_structure(
    "Please type password again.", 403)
ACCOUNT_REQUIRED = message_structure(
    "You don't have any account . please make one.", 404)
WRONG_DATA = message_structure(
    "wrong username or password.", 403)
