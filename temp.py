from os import listdir,path

path_name = r'C:\Work\LATools\EDCGFiona\target\my\recognize\cert1_forms-my_baseline'
f_list = listdir(path_name)
# print(type(f_list))
for index,f in enumerate(f_list):
    print(index,f)