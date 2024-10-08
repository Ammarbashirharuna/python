from pathlib import Path
from time import ctime
import shutil

path = Path("./modules/ecommerce/__init__.py")
print(path.exists())

#renaming path
# path.rename("apps.py")

#to check the information about the path
print(path.stat())

#ckeking the creation time of a file in readable format
print(ctime(path.stat().st_ctime))

#reading data from a file
print(path.read_text())
path.write_text("Am sorry am adding this text because i have forget about it")

#copying data from a file to another
source = Path("./modules/ecommerce/__init__.py")
target = Path("./modules/ecommerce/shopping/sales.py")
shutil.copy(source, target)


