from gpt import you
import re


def decode_unicode(m):
    return chr(int(m.group(1), 16))


def get_query(number_subjects: int, specification: str, interests: list) -> str:
    query = f"Write a list of {number_subjects} project topics in computer science on the theme of {specification} related to {[num for num in interests]}. Whitout introduction phrase and in row."
    try:
        res = you.Completion.create(prompt=query, detailed=True)
        res.text = re.sub(r'\\u([\da-fA-F]{4})', decode_unicode, res.text)
        return res
    except Exception as s:
        print(
            f'An error as occured : {s}, please check the get_query function in the get_query file.')


print(get_query(5, "Junior Programmer", {
      "Art", "Economic", "Sport"}).text)
