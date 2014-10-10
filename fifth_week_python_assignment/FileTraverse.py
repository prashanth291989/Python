import os
import fnmatch
import pickle

start_dir = "fortune1"
dirfileinfo=[]
filepathtemp=' '
filecontenttemp=' '
for dirpath, dirs, files in os.walk("fortune1"):
	for single_file in files:
		if fnmatch.fnmatch(single_file, "*txt"):
			filepathtemp=str(os.path.abspath(single_file));
			f = open(os.path.join(dirpath, single_file)) 
			filecontenttemp=str(f.read());
			temp=(filepathtemp,filecontenttemp);
			dirfileinfo.append(temp);
			f.close()


print(dirfileinfo);
output_file="raw_data.txt"
out=open(output_file,"ba")
pickle.dump(dirfileinfo,out)
out.close()
		
