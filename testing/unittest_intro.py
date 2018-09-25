"""
Unit Testing:

- Test smallest parts of an application in isolation (e.g. units)
- Good candidates for unit testing: individual classes,
modules, or functions
- Bad candidates for unit testing: an entire application,
dependencies across several classes or modules

Notes:

- unittest is a built-in module that comes with Python
- classes can inherit unittest.TestCase (encapsulation)
- run tests by running unittest.main()

"""


import unittest
from activities_units import eat, nap

class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        self.assertEqual(
            eat("broccoli", is_healthy=True),
            "I'm eating broccoli, because it is healthy!"
            )

    def test_eat_unhealthy(self):
        self.assertEqual(
            eat("pizza", is_healthy=False),
            "I'm eating pizza, because it tastes so good!"
            )

    def test_short_nap(self):
        self.assertEqual(
            nap(1), "Man, that was a short nap."
        )

    def test_long_nap(self):
        self.assertEqual(
            nap(3), "Whoops! I over slept..."
        )

if __name__ =="__main__":
    unittest.main()


# run this with -v for more verbosity