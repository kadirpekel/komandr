import sys
import inspect
import argparse
from functools import wraps
from itertools import izip_longest

routes = {}


def command(func):
    routes[func.__name__] = func
    return func


def execute(arg_list, version='0.0.1', **kwargs):
    parser = argparse.ArgumentParser(**kwargs)
    parser.add_argument('-v', '--version', action='version', version=version)
    subparsers = parser.add_subparsers()
    Positional = type('Positional', (object,), {})
    for route_name, func in routes.items():
        subparser = subparsers.add_parser(route_name)
        spec = inspect.getargspec(func)
        opts = reversed(list(izip_longest(reversed(spec.args or []),
                                          reversed(spec.defaults or []),
                                          fillvalue=Positional())))
        for k, v in opts:
            is_positional = isinstance(v, Positional)
            arg_name = k if is_positional else '--%s' % k
            arg = subparser.add_argument(arg_name)
            arg.required = v is None
            arg.default = v
        subparser.set_defaults(func=func)
    args = parser.parse_args(arg_list).__dict__
    func = args.pop('func')
    return func(**args)


def main(version='0.0.1', **kwargs):
    execute(sys.argv[1:], version, **kwargs)
