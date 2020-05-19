# response_code.py

from http_code_enum import HTTPCode
from http.client import HTTPResponse


def evaluate_response(response: HTTPResponse) -> str:
    if response.code() == HTTPCode.NOT_FOUND:
        return "Not Found"
    elif response.code() == HTTPCode.BAD_GATEWAY:
        return "???"
    elif response.code() == HTTPCode.BAD_REQUEST:
        return "???"
    else:
        return "Unknown Status Code"
