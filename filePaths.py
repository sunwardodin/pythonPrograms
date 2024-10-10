#!/usr/bin/env python3
import os
import datetime as dt
#os.remove("novel.txt")
#os.rename("first_draft.txt", "finished_masterpiece.txt")
print(os.path.exists("finished_masterpiece.txt"))
print(os.path.exists("finished_masterp.txt"))

print(os.path.getmtime("spider.txt"))

timestamp = os.path.getmtime("spider.txt")
#print(dt.dt.fromtimestamp(timestamp))

print(os.path.abspath("spider.txt"))
print(os.path.getsize("spider.txt"))