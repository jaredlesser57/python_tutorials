from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en>
<head>
    <meta charset="UTF-8">
    <title>First HTML Page</title>
</head>
<body>
    <div id="first">
        <h3 data-example="yes">hi</h3>
        <p>more text.</p>
    </div>
    <ol>
        <li class="special">This list item is special.</li>
        <li class="special">This list item is also special.</li>
        <li>This list item is not special.</li>
    </ol>
    <div>bye</div>
</body>
</html>
"""

# HTML TAG SELECTORS using find() and find_all()

soup = BeautifulSoup(html, "html.parser")
# print(soup.body)
# d = soup.find_all("div")
# print(d)
c = soup.find_all(class_="special") # or .special using select
print(c)
print()
i = soup.find(id="first") # or #first using select
print(i)
print()
a = soup.find_all(attrs={"data-example": "yes"}) # or [data-example] using select
print(a)

# CSS Style SELECTORS


print("=" * 50) # Seperator...

v = soup.select("#first")[0]
print(v)




### Accessing DATA

el = soup.select(".special")[0]
print(el)
print(el.get_text())

print()

for lines in soup.select(".special"):
    print(lines.get_text())