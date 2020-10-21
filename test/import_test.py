import sys
import imp

modules = ["Scatter"]

for each in modules:
    __import__(each)
    import_string = "import " + each
    exec(import_string)
    #aw = each.ApplicationWindow()
    #aw.show()

print(imp.find_module("Scatter"))
