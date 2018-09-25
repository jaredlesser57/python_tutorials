"""
Type examples (there are many more):

self.assertEqual(x, y)
self.assertNotEqual(x, y)
self.assertTrue(x)
self.assertFalse(x)
"""


# Can also assert for Errors (testing) Section 29, Lecure 299 (***Review as needed)

"""
class SomeTests(unittest.TestCase):
    def testing_for_error(self):
        '''testing for an error'''
        with seld.assertRaises(IndexError):
            l = [1,2,3]
            l[100]
"""

"""
Before and After Hooks - run before or after certain things occur (see below types)

setUp and tearDown:
- For larger applications, you may want similar application
state before running tests
- SetUp runs beforeeach test method
- tearDown runs after each test method
- Common use cases: adding/removing data from a test
database, creating instances of a class

Example:

----------------------------

def setUp(self):
    # do setup here
    pass

def test1(self):
    #setUp runs before
    #tearDown runs after
    pass

def test2(self):
    #setUp runs before
    #tearDown runs after
    pass

def tearDown(self):
    # do teardown here
    pass

----------------------------

"""

