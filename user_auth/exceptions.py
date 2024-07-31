from rest_framework.exceptions import APIException

class InvalidEmailException(APIException):
    status_code = 400
    default_detail = 'Invalid email address provided'
    default_code = 'Invalid_email'
    