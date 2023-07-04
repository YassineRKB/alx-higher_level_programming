#!/usr/bin/python3
def text_indentation(text):
    delimeters = [".", "?", ":"]
    TypeText = isinstance(text, str)
    lines = []
    final = "\n"
    if not TypeText:
        raise TypeError("text must be a string")
    for char in delimeters:
        text = text.replace(char, char + "\n\n")
    for line in text.split('\n'):
        line = line.strip(' ')
        lines.append(line)
    final = final.join(lines)
    print(final, end="")
