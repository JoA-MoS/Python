# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re


def email(val):
    pattern = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
    if pattern.match(val):
        return True
    else:
        return False


def first_name(val):
    # pattern = re.compile(r'([a-z]{2,})', re.UNICODE | re.IGNORECASE)
    # TODO: this condition doesn't allow accented characters need to fix
    if len(val) >= 2 and val.isalpha():
        return True
    else:
        return False


def last_name(val):
    # TODO: this condition doesn't allow accented characters need to fix
    if len(val) >= 2 and val.isalpha():
        return True
    else:
        return False


def password(val1, val2):
    if len(val1) >= 8 and val1 == val2:
        return True
    else:
        return False
