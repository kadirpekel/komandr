from komandr import main, command


@command
def foo(bar, baz=None):
    print 'foo', bar, baz

if __name__ == '__main__':
    main()
