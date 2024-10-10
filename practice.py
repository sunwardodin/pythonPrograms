#!/usr/bin/env python3
import areas as ar
import os

print("Hello, World!")

print(ar.rectangle(5, 5))

file= "novel.txt"
if os.path.isfile(file):
    print(os.path.isfile(file))
    print(os.path.getsize(file))
else:
	print(os.path.isfile(file), "File Not Found")