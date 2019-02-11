import os, sys, json

def buildDirectory(path):
    directory = {
        "name": os.path.basename(path),
        "path": path,
        "type": "Folder"
    }
    if (os.path.isfile(path)):
        directory["type"] = "File"
    else:
        directory["contents"] = [buildDirectory(os.path.join(path, subpath)) for subpath in os.listdir(path)]
    return directory

cmd_string_list = sys.argv
if (len(cmd_string_list) == 1):
    path = os.getcwd()
    print(json.dumps(buildDirectory(path), indent = 2))
else:
    path = cmd_string_list[1]
    if (os.path.exists(path) and os.path.isdir(path)):
        print(json.dumps(buildDirectory(path), indent = 2))
    else:
        print("Please enter a valid directory path string")
