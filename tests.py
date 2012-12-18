import unittest
import komandr


class TestRouterm(unittest.TestCase):

    def testRoute(self):
        def foo(bar, baz=None):
            return bar, baz
        komandr.command(foo)
        self.assertEqual(('1', '2'),
                         komandr.execute(['foo', '1', '--baz', '2']))


if __name__ == '__main__':
    unittest.main()
