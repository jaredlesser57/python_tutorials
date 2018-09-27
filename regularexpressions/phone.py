import re

def extract_phone(input):
    phone_regex = re.compile(r'\b\d{3}-\d{3}-\d{4}\b') # \b for boundaries
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None

print(extract_phone("my number is 301-275-3511"))
print(extract_phone("my number is 301-275-35111"))


def extract_all_phones(input):
    phone_regex = re.compile(r'\b\d{3}-\d{3}-\d{4}\b') # \b for boundaries
    return phone_regex.findall(input)

print(extract_all_phones("Reach me at 412-256-7639 or 412-965-3429"))



# def is_valid_phone(input):
#     phone_regex = re.compile(r'\b\d{3}-\d{3}-\d{4}\b') # \b for boundaries
#     match = phone_regex.search(input)
#     if match:
#         return match.group()
#     return None


def is_valid_phone(input):
    phone_regex = re.compile(r'\b\d{3}-\d{3}-\d{4}\b') # \b for boundaries
    match = phone_regex.fullmatch(input)
    if match:
        return match.group()
    return None

print("=" * 50)    

print(is_valid_phone("310-456-8294"))
print(is_valid_phone("310-456 8294"))
print(is_valid_phone("310-456-81294"))

