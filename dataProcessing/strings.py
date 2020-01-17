import re


def strings(content):
    list_ = re.findall("[a-zA-Z0-9]+", content)
    count = 0
    for item in list_:
        if len(item) >= 4:
            count += 1
    return count
