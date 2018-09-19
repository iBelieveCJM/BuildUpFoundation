# -*- coding: utf-8 -*-
"""
@author: CJM
"""

import time
from functools import wraps

def time_test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('--- {}ing starting...'.format(func.__name__))
        start = time.clock()    # use clock() instead of time() in windows
        result = func(*args, **kwargs)
        end = time.clock()
        print('--- {} costs {}'.format(func.__name__, end-start))
        return result
    return wrapper 