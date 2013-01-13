# TODO: Add much more tests
import unittest
import komandr
from mock import patch


class TestKomandr(unittest.TestCase):

    def tearDown(self):
        komandr.main.default_subcommand = None

    def testCommand(self):
        def foo(bar, baz=None):
            return bar, baz
        komandr.command(foo)
        self.assertEqual(('1', '2'),
                         komandr.execute(['foo', '1', '--baz', '2']))


    def testDefaultSubcommand(self):
        def foo(bar, baz=None):
            return bar, baz
        komandr.command(foo)

        # Without main.default_subcommand a `SystemExit` exception would raise.
        with self.assertRaises(SystemExit) as ex:
            komandr.execute([])

        self.assertEqual(2, ex.exception.code)

        # With main.default_subcommand='foo', subcommand named `foo` would be
        # called by default when no subcommand.
        komandr.main.default_subcommand = 'foo'
        self.assertEqual(('1', '2'), komandr.execute(['1', '--baz', '2']))

    def testDefaultSubcommandWithoutOptions(self):
        def foo():
            return 'bar'
        komandr.command(foo)

        komandr.main.default_subcommand = 'foo'
        self.assertEqual('bar', komandr.execute([]))

    def testOptionsNotTriggerDefaultSubcommand(self):
        def foo(baz='bar'):
            return baz
        komandr.command(foo)

        komandr.main.default_subcommand = 'foo'
        with patch.object(komandr.main.parser, 'print_help') as mock:
            with self.assertRaises(SystemExit) as ex:
                komandr.execute(['--help'])

        self.assertEqual(0, ex.exception.code)
        self.assertTrue(mock.called)

        self.assertEqual('bar baz', komandr.execute(['--baz', 'bar baz']))

if __name__ == '__main__':
    unittest.main()
