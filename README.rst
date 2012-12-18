=======
komandr
=======

komandr is a cool command-line framework which converts your ordinary functions
into cool command line interfaces.

Example
-------
::

    # example.py

    from komandr import main, command


    @command
    def foo(bar, baz=None):
        print 'foo', bar, baz

    if __name__ == '__main__':
        main()

Run your small program just typing::

    $ python example.py foo 1 --baz 2
    foo 1 2

Show help::

    $ python example.py --help
    usage: example.py [-h] [-v] {foo} ...

    positional arguments:
      {foo}

    optional arguments:
      -h, --help     show this help message and exit
      -v, --version  show program's version number and exit

Run command without mandatory args::

    $ python example.py foo
    usage: example.py foo [-h] --baz BAZ bar
    example.py foo: error: too few arguments


Cool, eh?

Status
------

Currently remains as a draft proposal, please stay tuned...

Licence
-------
Copyright (c) 2012 Kadir Pekel.

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the 'Software'), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
