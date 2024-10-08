from pathlib import Path
path = Path("./programs")
print(path.exists())


#iteerating over the path and print an object in each iteration
pathlist = [p for p in path.iterdir()]
print(pathlist)
#printing the directory 
pathlist = [p for p in path.iterdir() if p.is_dir()]
py_files = [p for p in path.glob("*.py")]
print(pathlist)
print(py_files)