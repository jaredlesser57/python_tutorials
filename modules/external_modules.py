# Use PIP (pip install) to install new external modules that are NOT built-in

# pip install termcolor

from termcolor import colored

text = colored("Hi There", color="cyan")

print(text)