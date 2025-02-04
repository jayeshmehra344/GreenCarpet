from git import Repo
import os

file_path = "C:\\Users\\Asus\\Desktop\\green-carpet\\Counter.txt"

with open(file_path, "r+") as file:
    text = file.read()
    num = int(text)
    file.seek(0)
    file.write(str(num + 1))
    file.truncate()

repo = Repo("C:\\Users\\Asus\\Desktop\\green-carpet\\")

repo.git.add("--all")
repo.index.commit("Update Counter.txt")

origin = repo.remote(name="origin")
origin.push()
