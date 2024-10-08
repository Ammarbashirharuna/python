from pathlib import Path

path = Path("./modules/ecommerce/__init__.py")
print(path.exists())
print(path.is_file())
print(path.is_dir())
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
#changin g the name of a path
path = path.with_name("file.txt")
#changing the extension of a path file using the suffix
path = path.with_suffix(".cpp")

print(path.suffix)
print(path.parent)


