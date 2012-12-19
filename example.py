from komandr import main, command


@command
def foo(bar, baz=None):
    print 'foo', bar, baz


@command(name='cool_command_name')
def lame_command_name(foo, bar, baz):
    print 'lame_command_name', foo, bar, baz

if __name__ == '__main__':
    main()
