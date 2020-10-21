#import sys
import glob
import Algorithm

if __name__ == '__main__':
   for filename in glob.glob(r'.\\Algorithm\\*.py'):
       filename = filename.replace('\\', '.')
       filename = filename[3:-3]
       obj = __import__(filename)
       #print(obj)
       #print(filename)
       c = getattr(obj, filename[10:])
       print(c)
       if hasattr(c, "name"):
           name = getattr(c, "name")
           print(name)
       if hasattr(c, "name"):
           name = getattr(c, "name")
           print(name)

   # p1 = ""
   # exec("p1 = Algorithm.linear.Predict_Main()")
   # print(p1.date)