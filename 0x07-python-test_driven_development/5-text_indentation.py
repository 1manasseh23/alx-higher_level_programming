#!/usr/bin/python3

def text_indentation(text):
    """
    This function prints a with 2 new line after each of these characters: .,? and :

    Args: n- text: a string represent the text to printed.

    Raise:
    - TypeError: if text is not a string.

    Returns:
    - None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        text = text.strip()
        for i in range(len(text)):
            if text[i] == '.' or text[i] == '?' or text[i] == ':':
                print(text[i])
                print()
            else:
                print(text[i], end='')
