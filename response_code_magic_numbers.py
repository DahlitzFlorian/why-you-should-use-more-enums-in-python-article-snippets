# response_code_magic_numbers.py

from http.client import HTTPResponse


def evaluate_response(response: HTTPResponse) -> str:
    if response.code() == 404:
        return "Not Found"
    elif response.code() == 502:
        return "???"
    elif response.code() == 400:
        return "???"
    else:
        return "Unknown Status Code"
