import sys
import glob

def filename_list():
    Modules = []
    for filename in glob.glob(r'.\Algorithm\*.py'):
        filename = filename.replace('\\','.')
        Modules.append(filename[2:-3])
        #print(filename[2:-3])
    return Modules

if __name__ == '__main__':
    modules = filename_list()
    #print(modules)
    #import_string = 'import Algorithm.AverValue'
    for each in modules:
        obj = __import__(each)
        #print(obj)
        #import_string = "import " + each
        #exec(import_string)
        # aw = each.ApplicationWindow()
        # aw.show()
    #print(sys.modules)
    #exec("print(Algorithm.BPpower.name == None)")