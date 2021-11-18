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

    def testMultipleValuesForASingleArgument(self):

        def bar(c=[]):
            return c
        komandr.command(bar)

        self.assertEqual(['blue', 'red', ], komandr.execute(['bar', '--c', 'blue', '--c', 'red']))


if __name__ == '__main__':
    unittest.main()
