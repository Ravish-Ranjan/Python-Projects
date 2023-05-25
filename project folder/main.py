from os import scandir
from tkinter.filedialog import askdirectory
import json

folderpath = askdirectory(title="Select folder of which you want to get data")


dir = {}

def traverser(fold):
    data = scandir(fold)
    folders = []
    files = []
    for node in data:
        if node.is_dir():
            folders.append(node.name)
        elif node.is_file:
            files.append(node.name)
    res = []
    if len(folders) != 0:
        for subfold in folders:
            res.append(traverser(fold+"/"+subfold))
    locdir = {
        "root":fold.replace("/","//").replace("\\","//"),
        "files":files,
        "folders":res
    }
    return locdir

# print(traverser(folderpath))

destfold = askdirectory(title="Select the folder in which the data is going to be saved")

with open(destfold+"/scandir.json",'w') as jsn:
    obj = json.dumps(traverser(folderpath),indent=4)
    jsn.write(obj)