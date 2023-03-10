# importing required modules 
import os
import datetime
  
# folder is the name of the folder in which we have to perform the delete operation
folder = "C:/Users/ADMIN/Downloads"
  
# days is the number of days for which we have to check whether the file is older than the specified days or not 
days = 30
  
# function to perform delete operation based on condition
def check_and_delete(folder):
   # loop to check all files one by one 
   # os.walk returns 3 things: current path, files in the current path, and folders in the current path 
   for (root,dirs,files) in os.walk(folder, topdown=True):
       for f in files:
           # temp variable to store path of the file 
           file_path = os.path.join(root,f)
           # get the timestamp, when the file was modified 
           timestamp_of_file_modified = os.path.getmtime(file_path)
           # convert timestamp to datetime
           modification_date = datetime.datetime.fromtimestamp(timestamp_of_file_modified)
           # find the number of days when the file was modified
           number_of_days = (datetime.datetime.now() - modification_date).days
           if number_of_days > days:
               # remove file 
               os.remove(file_path)
               print(f" Delete : {f}")
  
# call function
check_and_delete(folder)


