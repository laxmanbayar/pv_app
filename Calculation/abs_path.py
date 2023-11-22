import os.path
from Variables import var
# print("in abs path.py")


# cur_dir = os.path.dirname(os.path.abspath(__file__))
# print(cur_dir)
# print(">>>>>>>>>>>>>>>>>>>>>>>")
# # while not os.path.exists(os.path.join(cur_dir, "main.py")):
# #         cur_dir = os.path.dirname(cur_dir)
# #         print(f"cur dir {cur_dir}")
        
# root_dir =os.path.join(cur_dir,"main.py")
# print(root_dir)


def absolute_path(path):
 #print("in abs path func ")       
 #abs_path= os.path.join(cur_dir, path)
 abs_path=os.path.join(var.root_dir_path, path)
 return abs_path
