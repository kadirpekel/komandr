from komandr import *


# straigforward ad-hoc usage
@command
def foo(bar, baz=None):
    print 'foo', bar, baz


# but also it allows you much more tuning
@command(name='cool_command_name')
@arg('baz', '-z', required=True, type=int)
def lame_command_name(foo, bar, baz=1):
    print 'lame_command_name', foo, bar, baz

if __name__ == '__main__':
    main()
