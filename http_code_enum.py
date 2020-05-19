# http_code_enum.py

from enum import IntEnum


class HTTPCode(IntEnum):
    BAD_REQUEST = 400
    NOT_FOUND = 404
    BAD_GATEWAY = 502
