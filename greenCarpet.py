from git import Repo
import os

file_path = "Counter.txt"

with open(file_path, "r+") as file:
    text = file.read()
    num = int(text)
    file.seek(0)
    file.write(str(num + 1))
    file.truncate()

repo = Repo("D:\\Python-For-Git\\")

repo.git.add("--all")
repo.index.commit("Update Counter.txt")

origin = repo.remote(name="origin")

origin.push()
