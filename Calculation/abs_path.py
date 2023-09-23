import os.path

cur_dir = os.path.dirname(os.path.abspath(__file__))
#print(">>>>>>>>>>>>>>>>>>>>>>>")
while not os.path.exists(os.path.join(cur_dir, "main.py")):
        cur_dir = os.path.dirname(cur_dir)
        
root_dir =os.path.join(cur_dir,"main.py")
#print(root_dir)


def absolute_path(path):
 abs_path= os.path.join(cur_dir, path)
 return abs_path
