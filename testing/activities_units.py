"""
This file is used with unittest_intro.py to display how unittests in Python work
"""

def eat(food, is_healthy):
    ending = "because it tastes so good!"
    if is_healthy:
        ending = "because it is healthy!"
    return(f"I'm eating {food}, {ending}")

def nap(num_hours):
    if num_hours > 2:
        return f"Whoops! I over slept..."
    return "Man, that was a short nap."