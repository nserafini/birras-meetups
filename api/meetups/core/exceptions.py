from fastapi import HTTPException

class HandledException(HTTPException):

    default_message = "Ups! There was an error."
    status_code = 500

    def __init__(self, resource: str, message: str = None):
        if not message:
            message = self.default_message
        super().__init__(status_code=self.status_code, detail=message.format(resource))

    def __str__(self):
        return self.__class__.__name__


class ResourceNotFound(HandledException):
    default_message = "Resource {} not found."
    status_code = 404
    
class UnauthorizedRequest(HandledException):
    default_message = "Invalid Api Key: {}"
    status_code = 401

class InvalidAuth(HandledException):
    default_message = "Failed Auth: invalid {}"
    status_code = 403

class ForbiddenNotLogged(HandledException):
    default_message = "Forbidden: Not logged"
    status_code = 403

class ForbiddenNoAdminRole(HandledException):
    default_message = "Forbidden: Only admin allowed"
    status_code = 403