import string
import re

# def strings(filename, min=4):
#     #with open(filename, errors="ignore") as f:  # Python 3.x
#     result = ""
#     for c in filename:
#         if c in string.printable:
#             result += c
#             continue
#         if len(result) >= min:
#             yield result
#         result = ""
#     if len(result) >= min:  # catch result at EOF
#         yield result

# def strings(content):
#     return len(re.findall("[^\x00-\x1F\x7F-\xFF]{4,}", content))

