#!/usr/bin/env python
__author__ = 'ziyan.yin'

import datetime
import string


def is_empty(arg):
    """
        string is None or ''
            >>> is_empty('a')
    """
    if arg is None:
        return True
    if str(arg).strip() == '':
        return True
    return False


def is_number(arg: str):
    """
        string is number like 1.0, -1
            >>> is_number('1.5')
    """
    if len(arg) > 1 and arg[0] == '0':
        return False
    if arg.startswith('-'):
        arg = arg[1:]
    if arg.isdigit():
        return True
    if arg.find('.') > 0:
        args = arg.split('.')
        if len(args) > 0 and args[0].isdigit() and args[1].isdigit():
            return True
    return False


def is_digit(arg: str):
    """
        isdigit() method
    """
    return arg.isdigit()


def is_bool(arg: str):
    """
        check if string is true or false
            >>> is_bool('true')
    """
    if arg in ('true', 'false'):
        return True
    return False


def is_date(arg: str, base='%Y-%m-%d %H:%M:%S'):
    """
        check if string is date-format
            >>> is_date('2020-01-01 00:00:00')
    """
    try:
        datetime.datetime.strptime(arg, base)
        return True
    except (TypeError, ValueError):
        return False


def is_chinese(arg: str):
    """
        check if string is utf-8 chinese
            >>> is_chinese('我')
    """
    for ch in arg:
        if u'\u4e00' <= ch <= u'\u9fa5':
            return True
    return False


def is_letter(arg: str):
    """
        check if string is number or words
            >>> is_letter('ab12123')
    """
    for ch in arg:
        if ch not in frozenset(string.ascii_letters + string.digits):
            return False
    return True


def is_tag(arg: str):
    """
        check if string is tag format
            >>> is_tag('Abc_1234')
    """
    for ch in arg:
        if ch not in frozenset(string.ascii_letters + string.digits + '_'):
            return False
    return True


def is_label(arg: str):
    """
        check if string is sql column format
            >>> is_label('ab12123')
    """
    if len(arg) > 0 and arg[0] in frozenset(string.digits):
        return False
    for ch in arg:
        if ch not in set(string.ascii_letters + string.digits + '_'):
            return False
    return True


def is_legal(arg: str):
    """
        check if string has illegal word
            >>> is_legal('ab12123')
    """
    illegal_signal = frozenset('~|')
    for ch in arg:
        if ch in illegal_signal:
            return False
    return True
