import re

titles = [
    "Significant Others (1987)",
    "Tales of the City (1978)",
    "The Days of Anna Madrigal (2014)",
    "Mary Ann in Autumn (2010)",
    "Further Tales of the City (1982)",
    "Babycakes (1984)",
    "More Tales of the City (1980)",
    "Sure of You (1989)",
    "Michael Tolliver Lives (2007)"
]
fixed_titles = []

titles.sort()
# print(titles)

# pattern = re.compile(r'(^[\w ]+) (\(\d{4}\))')
# result = pattern.sub("\g<2> - \g<1>", titles[0])
# print(result)

pattern2 = re.compile(r'(?P<title>^[\w ]+) \((?P<date>\d{4})\)')
for book in titles:
    result2 = pattern2.sub("\g<2> - \g<1>", book) # or \g<date> - \g<title>
    fixed_titles.append(result2)
fixed_titles.sort()
print(fixed_titles)