
#!/usr/bin/python3
"""Function that appends a string at the end of a text file and returns the number of characters added."""


def append_write(filename="", text=""):
    """append a string to text.
    """
    with open(filename, 'a') as f:
        return f.append(text)
