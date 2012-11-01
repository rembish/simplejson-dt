from simplejson import load as _load, dump as _dump, loads as _loads, dumps as _dumps
from dateutil.parser import parse

__all__ = ['load', 'loads', 'dump', 'dumps']

class EncoderMixin:
    pass

class DecoderMixin:
    pass

def load(fp, parse_date=None, **kwargs):
    return _load(fp, **kwargs)

def dump(obj, fp, parse_date=None, **kwargs):
    return _dump(obj,fp, **kwargs)

def loads(s, parse_date=None, **kwargs):
    return _loads(s, **kwargs)

def dumps(obj, parse_date=None, **kwargs):
    return _dumps(obj, **kwargs)
