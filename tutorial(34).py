# name= "     Yunesh     "
# dots = "................."
# # lstrip() method
# print(name + dots)
# print(name.lstrip() + dots)
# print(name.rstrip() +dots)
# print(name.strip() +dots)
# print(name.replace(" ","")+ dots)

name, char =input("enter comma separated name and character : ").split(",")
print(f"length of your name is {len(name)}")
print(f"character count : {name.strip().count(char.strip.lower())}") # case sensitive
# Yunesh - yunesh
# " Yunesh "-------->"Yunesh"------> "yunesh"
# "  H  "-------->"H"------->"h"
# name.strip().count(char.strip.lower())
# char.strip.lower()