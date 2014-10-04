from datetime import datetime
import shelve
def search(d):
	query=input("query:")
	dt1= datetime.now()
	listquery=query.split(" ")
	orcount=0;andcount=0;
	searchkeys=set(listquery)

	for item in searchkeys:
		if(item=='or'):
			orcount+=1;	
		elif(item =='and'):
			andcount+=1;	
		
	if(orcount>=1):
		searchkeys.remove('or');
	if(andcount>=1):
		searchkeys.remove('and');
		
	result=set();
	dic = shelve.open(d);
	if(((orcount>=1) and (andcount>=1)) or (andcount>=1) or ((orcount==0) and (andcount==0))):
		for k in searchkeys:
			if k in dic.keys():
				temp=dic[k]
				if(len(result)==0):
					result=temp;
				else:
					result=result&temp;
			else:
				print("keyword not found");
	else:
		for k in searchkeys:
			if k in dic.keys():
				temp=dic[k]
				if(len(result)==0):
					result=temp;
				else:
					result=result|temp;
			else:
				print("keyword not found");
	
	print(result);
	dt2= datetime.now()
	print("Execution time:", dt2.microsecond-dt1.microsecond)