#!/usr/bin/python3
def read_file(filename=""):
    if not filename:
        return

    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
