import pickle
from os.path import exists

if exists("formdata_set.pkl"):
    with open("formdata_set.pkl", "rb") as pkl_file:
        formdata_set = pickle.load(pkl_file)
else:
    formdata_set = set()
    

for formdata in formdata_set:
    print(formdata)
    
print(len(formdata_set))