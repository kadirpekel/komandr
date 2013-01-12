# TODO: Add much more tests
import unittest
import komandr


class TestKomandr(unittest.TestCase):

    def testCommand(self):
        def foo(bar, baz=None):
            return bar, baz
        komandr.command(foo)
        self.assertEqual(('1', '2'),
                         komandr.execute(['foo', '1', '--baz', '2']))


    def testMainDefault(self):
        def foo(bar, baz=None):
            return bar, baz
        komandr.command(foo)

        # Without main.default a SystemExit exception would be raised.
        with self.assertRaises(SystemExit) as ex:
            komandr.execute([])

        self.assertEqual(2, ex.exception.code)

        # With main.default=foo, `foo` would be called by default when no subcommand.
        import functools
        komandr.main.default = functools.partial(foo, bar='1', baz='2')
        self.assertEqual(('1', '2'), komandr.execute([]))


if __name__ == '__main__':
    unittest.main()
