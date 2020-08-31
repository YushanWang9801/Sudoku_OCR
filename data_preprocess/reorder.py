import os
import re
init_path = 'C:/Users/yusha/Desktop/Sodoku_OCR/data/60_Sudokus_New_Medium/'
os.chdir(os.path.dirname(init_path))
arr = os.listdir()
start_Num = 0

'''
for i in arr:
    s = i.split(".")
    s = int(s[0]) 
    if s > start_Num:
        start_Num = s
#print(start_Num)
'''

#print(arr)
dict = {}
for i in arr:
    s = i.split(".")
    s = int(s[0]) 
    dict[s] = i

counter = 0
for key in sorted(dict):
    counter += 1 
    new_name = init_path+str(counter)+'.jpg'
    os.rename(dict[key], new_name)

print("reorder finished")
