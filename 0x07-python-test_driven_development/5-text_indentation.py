#!/usr/bin/python3
''' This is the module for text_indentation(text) '''


def text_indentation(text):
    ''' Args:
            text: text to be split
        Return: Multiple lines split by , ? :
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    changed_text = ""

    for character in range(len(text)):
        if text[character] in [".", "?", ":"]:
            changed_text += text[character] + "\n\n"
        elif text[character - 1] == "." and text[character] == " ":
            pass
        else:
            changed_text += text[character]

    print(changed_text, end="")
