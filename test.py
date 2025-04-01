import re

text = "foo <skip>foo</skip> foo"

def conditional_replace(match):
    start = match.start()
    if re.search(r"<skip>.*?foo.*?</skip>", text):
        span = re.search(r"<skip>.*?foo.*?</skip>", text).span()
        # If this match is inside the skip zone, return it unchanged
        if span[0] <= start < span[1]:
            return match.group()
    return "bar"

result = re.sub(r"foo", conditional_replace, text)
print(result)  # Output: bar <skip>foo</skip> bar

# use this to split the input by : and begin piping logic#