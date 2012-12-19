# -*- coding: utf-8 -*-
"""Simple module helps you convert your oridnary functions into cool
command-line interfaces using :py:module:``argparse`` in backyard.

"""
import sys
import inspect
import argparse
from functools import wraps
from itertools import izip_longest


class prog(object):
    """Class to hold an isolated command registry and execution blocks to keep
    them within the same namespace.

    """
    _COMMAND_FLAG = '_command'
    _POSITIONAL = type('_positional', (object,), {})

    def __init__(self, version='0.0.1', **kwargs):
        """Constructor

        :param version: program version
        :param type: str

        :param **kwargs: keyword arguments those passed through to
                         :py:class:``argparse.ArgumentParser`` constructor
        :param type: dict

        """
        self.parser = argparse.ArgumentParser(**kwargs)
        self.parser.add_argument('-v', '--version', action='version',
                                 version=version)
        self.subparsers = self.parser.add_subparsers()

    def command(self, *args, **kwargs):
        """Convenient decorator function which simply registers a function into
        command registry.

        """
        if len(args) == 1 and callable(args[0]):
            return self._generate_command(args[0])
        else:
            def _command(func):
                return self._generate_command(func, *args, **kwargs)
            return _command

    def arg(self, arg_name, *args, **kwargs):
        """Convenient decorator function which simply configures any arg by
        given arg_name with supplied args and kwargs passing them transparently
        to :py:func:``argparse.ArgumentParser.add_argument`` interface

        :param arg_name: arg name to configure
        :param type: str

        """
        def wrapper(func):
            if not getattr(func, 'argopts', None):
                func.argopts = {}
            func.argopts[arg_name] = (args, kwargs)
            return func
        return wrapper

    def _generate_command(self, func, name=None):
        """Generates a command parser for given func.

        :param func: func to generate related command parser
        :param type: function

        """
        subparser = self.subparsers.add_parser(name or func.__name__)
        spec = inspect.getargspec(func)
        opts = reversed(list(izip_longest(reversed(spec.args or []),
                                          reversed(spec.defaults or []),
                                          fillvalue=self._POSITIONAL())))
        for k, v in opts:
            argopts = getattr(func, 'argopts', {})
            args, kwargs = argopts.get(k, ([], {}))
            args = list(args)
            is_positional = isinstance(v, self._POSITIONAL)
            options = [arg for arg in args if arg.startswith('-')]
            if is_positional:
                if options:
                    args = options
                    kwargs.update({'required': True, 'dest': k})
                else:
                    args = [k]
            else:
                args = options or ['--%s' % k]
                kwargs.update({'default': v, 'dest': k})
            arg = subparser.add_argument(*args, **kwargs)
        subparser.set_defaults(**{self._COMMAND_FLAG: func})
        return func

    def execute(self, arg_list):
        """Main function to parse and dispatch commands by given arg_list after
        generating corresponding parser for each one.

        :param arg_list: all arguments provided by the command line
        :param type: list

        """
        arg_map = self.parser.parse_args(arg_list).__dict__
        command = arg_map.pop(self._COMMAND_FLAG)
        return command(**arg_map)

    def __call__(self):
        """Calls :py:func:``execute`` with :py:class:``sys.argv`` excluding
        executing script name arg which comes as first one.

        """
        self.execute(sys.argv[1:])

main = prog()
arg = main.arg
command = main.command
execute = main.execute
