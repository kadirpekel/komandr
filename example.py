from komandr import *


@command
def foo(bar, baz=None):
    print('foo', bar, baz)


@command(name='cool_command')
@arg('baz', '-z', required=True, type=int)
def lame_command(foo, bar, baz=1):
    print('lame_command', foo, bar, baz)

main()
