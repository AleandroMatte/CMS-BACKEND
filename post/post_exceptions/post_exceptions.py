from rest_framework import status


class PostException(Exception):
    def __init__(self, message, status_code, *args):
        self.message = message
        self.status = status_code
        super().__init__(*args)


class DuplicatedPostNameException(PostException):
    def __init__(self, message, status_code, *args):
        status_code = status.HTTP_400_BAD_REQUEST
        super().__init__(message, status_code, *args)
