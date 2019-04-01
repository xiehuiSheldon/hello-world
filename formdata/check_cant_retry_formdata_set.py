import pickle
from os.path import exists

if exists("cant_retry_formdata_set.pkl"):
    with open("cant_retry_formdata_set.pkl", "rb") as pkl_file:
        cant_retry_formdata_set = pickle.load(pkl_file)
else:
    cant_retry_formdata_set = set()
    

for cant_retry_formdata in cant_retry_formdata_set:
    print(cant_retry_formdata)
    
print(len(cant_retry_formdata_set))