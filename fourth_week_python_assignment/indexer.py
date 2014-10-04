import re
import pickle
import shelve

def process_data(data,newdbfile):	
	tempstr=""
	dic={}
	keywords=[]
	words=[]
	data_list=[]
	str1=''
	str2=''
	f=open(data,"br")
	data_list=pickle.load(f)
	for quote in data_list:
		words.extend(quote[1].split());	
		
	for word in words:
		tempstr= re.sub('[^A-Za-z0-9]+', '', word)
		keywords.append(tempstr)
	keywords=list(keywords);
	
	for word in keywords:
		for quote in data_list:
			if word in quote[1]:
				if word in dic.keys():
					dic[word].add(quote[0])
				else:
					dic[word] = set([quote[0]])
	file=shelve.open(newdbfile);
	for d,f in dic.items():
		file[d]=f
	file.close();
	return dic;		