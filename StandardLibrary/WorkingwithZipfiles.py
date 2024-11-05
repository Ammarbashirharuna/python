from pathlib import Path
from zipfile import ZipFile

# with ZipFile("files.zip", "w") as zip:
#       for path in Path("../programs").rglob("*.*"):
#         zip.write(Path)
#reading the data from the zipfile
with ZipFile("files.zip") as zip:
     print(zip.namelist())


#extracting from zip file
zip.extractall("Extract")