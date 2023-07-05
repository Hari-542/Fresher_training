import pandas as  pd
import glob
path1=input("enter the csv file path 1:")
path2=input("enter the csv file path 2:")
destination_path=input("Enter destination csv file path:")
emp_csv=pd.read_csv(path1)
exp_csv=pd.read_csv(path2)
merge_csv=pd.merge(emp_csv,exp_csv,on="id",how="outer").fillna("NaN")
merge_csv.to_csv(destination_path)
print(merge_csv)