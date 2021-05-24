#!/usr/bin/env python
__author__ = 'ziyan.yin'

import hashlib
import hmac
import base64
from typing import Union


def md5(content: str):
    m = hashlib.md5()
    m.update(content.encode())
    return m.hexdigest()


def hmac_md5(content: Union[str, bytes], key: bytes = b''):
    if type(content) is str:
        content = content.encode()
    m = hmac.new(key, content, digestmod=hashlib.md5)
    return m.hexdigest()


def sha1(content: Union[str, bytes]):
    sha = hashlib.sha1()
    if type(content) is str:
        content = content.encode()
    sha.update(content)
    return sha.hexdigest()


def hmac_sha1(content: Union[str, bytes], key: bytes = b''):
    if type(content) is str:
        content = content.encode()
    m = hmac.new(key, content, digestmod=hashlib.sha1)
    return m.hexdigest()


def sha256(content: str):
    sha = hashlib.sha256()
    sha.update(content.encode())
    return sha.hexdigest()


def hmac_sha256(content: Union[str, bytes], key: bytes = b''):
    if type(content) is str:
        content = content.encode()
    m = hmac.new(key, content, digestmod=hashlib.sha256)
    return m.hexdigest()


def b64encode(content: Union[str, bytes]):
    return base64.b64encode(content)


def b64decode(content: Union[str, bytes]):
    return base64.b64decode(content)
