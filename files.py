#!/usr/bin/env python3
with open("spider.txt") as file:
    for line in file:
        print(line.upper())

with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())

file = open("spider.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)

with open("novel.txt", "w") as file:
    file.write("It was a dark and stormy night")

# "r": read only, "w": write only, "a": append, "r+": read and write
# Be warned, if you open a file with w and there were contents in there, the old contents will be destroyed.