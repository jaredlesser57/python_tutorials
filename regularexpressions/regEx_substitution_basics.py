import re

text = "Last night Mrs. Daisy and Mr. White murdered Mr. Crow. Miss White was a witenence."

pattern = re.compile(r'(Mr\.|Ms\.|Mrs\.|Miss) ([a-z])[a-z]+', re.I)
print(pattern.findall(text))
print(pattern.search(text).group())
print()

result = pattern.sub("REDACTED", text)
print(result)

result2 = pattern.sub("\g<1> REDACTED", text)
print(result2)

result3 = pattern.sub("\g<1> \g<2>", text)
print(result3)
