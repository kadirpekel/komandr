=======
komandr
=======

Convert your ordinary functions into cool command-line interfaces!

Komandr is a smart thin wrapper around powerful ``argparse`` module lets you
build defacto standart command-line interfaces in secondz while providing you
all the flexibity.

Example
-------

.. code-block:: python

    from komandr import *

    @command
    def foo(bar, baz=None):
        print 'foo', bar, baz

    main()


Need some help?

.. code-block:: console

    $ python example.py --help
    usage: example.py [-h] [-v] {foo,cool_command} ...

    positional arguments:
      {foo,cool_command}

    optional arguments:
      -h, --help            show this help message and exit
      -v, --version         show program's version number and exit

Let's investigate more about ``foo``

.. code-block:: console

    $ python example.py foo --help
    usage: example.py foo [-h] --baz BAZ bar

    positional arguments:
      bar

    optional arguments:
      -h, --help  show this help message and exit
      --baz BAZ

Test ``foo`` command

.. code-block:: console

    $ python example.py foo Hello
    usage: example.py foo [-h] --baz BAZ bar
    example.py foo: error: argument --baz is required

That's ok now

.. code-block:: console

    $ python example.py foo Hello --baz World
    foo Hello World

Cool, eh? What if you need more control over?

.. code-block:: python

    from komandr import *

    @command('cool_command')
    @arg('baz', '-z', required=True, type=int)
    def lame_command(foo, bar, baz=1):
        print 'lame_command', foo, bar, baz

    main()

Let's try it

.. code-block:: console

    $ python example.py cool_command Hello -z 'wtf' World
    usage: example.py cool_command [-h] --baz BAZ foo bar
    example.py cool_command: error: argument --baz/-z: invalid int value: 'wtf'

Correct one should be

.. code-block:: console

    $ python example.py cool_command Hello -z 2013 World
    lame_command Hello World 2013

Showcase
--------

Want to see something real, Checkout Dudu https://github.com/kadirpekel/dudu

Enjoy!

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
