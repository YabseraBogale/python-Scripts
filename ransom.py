"""
why does python have this much control on the os ?

"""
import shutil as sh
try:
    sh.rmtree("test")
except FileNotFoundError as e:
    print(str(e))
