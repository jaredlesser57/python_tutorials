import re

def parse_name(input):
    name_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) ([A-Za-z]+)$')
    matches = name_regex.search(input)
    print(matches.group(0))
    print(matches.group(1))
    print(matches.group('first')) # this can be done as well (label)
    print(matches.group(2)) # this can be done as well
    print(matches.group(3))

parse_name("Mr. Jared Lesser")

