from git import Repo
import os

file = open("Counter.txt", "r+")
text = file.read()
num = int(text)
file.write(str(num + 1))
