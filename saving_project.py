import os

os.makedirs("saving_project", exist_ok=True)
print("Folder kerja saat ini:", os.getcwd())
print("Isi folder saving_project:", os.listdir("saving_project"))