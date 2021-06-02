#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'ziyan.yin'

import datetime
import decimal
from dataclasses import is_dataclass, asdict
from enum import Enum
from typing import Union
import json


def json_default(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    elif isinstance(obj, datetime.datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(obj, datetime.date):
        return obj.strftime('%Y-%m-%d')
    elif is_dataclass(obj):
        return asdict(obj)
    elif issubclass(obj.__class__, Enum):
        return obj.name
    elif getattr(obj, '__json__'):
        return obj.__json__()


def dumps(data):
    """
        dict to json
    """
    return json.dumps(data, default=json_default)


def loads(data: Union[str, bytes]):
    """
        json to dict
    """
    try:
        return json.loads(data)
    except (json.JSONDecodeError, TypeError):
        raise ValueError
