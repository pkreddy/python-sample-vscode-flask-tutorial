print(" ******* python syntax test begins *********")

import glob
import os
import py_compile

my_path = os.getcwd()
main_folder = "proj"
files = glob.iglob(my_path + '/'+main_folder+'/**/*.py', recursive=True)

for i in files:
    print(i)
    py_compile.compile(i)


print(" ******* python syntax test ends *********")