=======
komandr
=======

Convert your ordinary functions into cool command-line interfaces.

Example
-------
::

    # example.py

    from komandr import main, command


    @command
    def foo(bar, baz=None):
        print 'foo', bar, baz


    @command(name='cool_command_name')
    def lame_command_name(foo, bar, baz):
        print 'lame_command_name', foo, bar, baz

    if __name__ == '__main__':
        main()


Need some help?::

    $ python example.py --help
    usage: example.py [-h] [-v] {foo,cool_command_name} ...

    positional arguments:
      {foo,cool_command_name}

    optional arguments:
      -h, --help            show this help message and exit
      -v, --version         show program's version number and exit

Let's investigate more about `foo`::

    $ python example.py foo --help
    usage: example.py foo [-h] --baz BAZ bar

    positional arguments:
      bar

    optional arguments:
      -h, --help  show this help message and exit
      --baz BAZ

Test `foo` command::

    $ python example.py foo Hello
    usage: example.py foo [-h] --baz BAZ bar
    example.py foo: error: argument --baz is required

That's ok now::

    $ python example.py foo Hello --baz World
    foo Hello World

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
