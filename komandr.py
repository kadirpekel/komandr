# -*- coding: utf-8 -*-
"""Simple module helps you convert your oridnary functions into cool
command-line interfaces using :py:module:``argparse`` in backyard.

"""
import sys
import inspect
import argparse


class prog(object):
    """Class to hold an isolated command namespace"""

    _COMMAND_FLAG = '_command'

    def __init__(self, version='2.0.1', **kwargs):
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
        """Convenient decorator simply creates corresponding command"""
        if len(args) == 1 and callable(args[0]):
            return self._generate_command(args[0])
        else:
            def _command(func):
                return self._generate_command(func, *args, **kwargs)
            return _command

    def arg(self, arg_name, *args, **kwargs):
        """Decorator function configures any arg by given ``arg_name`` with
        supplied ``args`` and ``kwargs`` passing them transparently to
        :py:func:``argparse.ArgumentParser.add_argument`` function

        :param arg_name: arg name to configure
        :param type: str

        """
        def wrapper(func):
            if not getattr(func, 'argopts', None):
                func.argopts = {}
            func.argopts[arg_name] = (args, kwargs)
            return func
        return wrapper

    def _parse_docstring(self, func):
        if not func.__doc__:
            return
        try:
            from gdparser import parse
        except ImportError:
            return
        return parse(func.__doc__, remove_indent=True)

    def _generate_command(self, func, name=None, **kwargs):
        """Generates a command parser for given func.

        :param func: func to generate related command parser
        :param type: function

        :param name: command name
        :param type: str

        :param **kwargs: keyword arguments those passed through to
                         :py:class:``argparse.ArgumentParser.add_parser``
        :param type: dict

        """

        doc = self._parse_docstring(func)
        if doc and not 'description' in kwargs:
            kwargs['description'] = doc.get('description')

        subparser = self.subparsers.add_parser(name or func.__name__, **kwargs)
        
        sig = inspect.signature(func)

        # Check whether this function is a bound class method
        is_self_bound = getattr(func, '__self__', None)

        for k, v in sig.parameters.items():
            # Skip the parameter `self` if we are self bound
            if is_self_bound and k == 'self':
                continue

            argopts = getattr(func, 'argopts', {})
            args, kwargs = argopts.get(k, ([], {}))
            args = list(args)
            options = [arg for arg in args if arg.startswith('-')]

            assert v.kind is v.POSITIONAL_OR_KEYWORD, \
                'Variable length args are not supported.'

            if doc:
                params = doc.get('parameters', [])
                for param in params:
                    if param['name'] == k:
                        kwargs['help'] = param.get('description')

            if v.default is v.empty:
                if options:
                    args = options
                    kwargs.update({'required': True, 'dest': k})
                else:
                    args = [k]
            else:
                args = options or ['--%s' % k]
                kwargs.update({'default': v.default, 'dest': k})


            if v.annotation is not v.empty:
                kwargs['type'] = v.annotation

            # If type is bool, do some special treatment
            if v.annotation == bool:
                kwargs['action'] = 'store_true'

            # If type is list, assume all contained types as str
            if v.annotation == list:
                kwargs['type'] = str
                kwargs['action'] = 'extend'
                kwargs['nargs'] = '+'

            subparser.add_argument(*args, **kwargs)
        subparser.set_defaults(**{self._COMMAND_FLAG: func})
        return func

    def execute(self, arg_list):
        """Main function to parse and dispatch commands by given ``arg_list``

        :param arg_list: all arguments provided by the command line
        :param type: list

        """
        if not arg_list:
            arg_list = ['--help']

        arg_map = self.parser.parse_args(arg_list).__dict__
        command = arg_map.pop(self._COMMAND_FLAG)
        return command(**arg_map)

    def __call__(self):
        """Calls :py:func:``execute`` with :py:class:``sys.argv`` excluding
        script name which comes first.

        """
        self.execute(sys.argv[1:])


main = prog()
arg = main.arg
command = main.command
execute = main.execute
