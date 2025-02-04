from git import Repo
import os

file = open("Counter.txt", "r+")
file.write('Hello')
for i in range(10):
    file.write(str(i))