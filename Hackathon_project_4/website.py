from wsgiref.simple_server import make_server
from flask import Flask,jsonify,request
import sqlite3

message1="<html><head><meta charset="+"UTF-8"+"><title>Professor rating</title></head><body  bgcolor="+"#CEF6F5"+"><hr/><h1 bgcolor="+"#CEF6F5"+" align="+"center"+">RATE MY PROFESSOR</h1>"	
message2="<hr/><div align="+"center"+"><form action="+"http://127.0.0.1:5000/insertintodb"+" method="+"GET"+"><table><tr ><td><label>Professor &nbsp;&nbsp;&nbsp;&nbsp;	:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label>"

message3="<input type="+"text"+" name="+"professor"+"></td></tr><br><tr><td><label>School &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label><input type="+"text"+" name="+"School"+"></tr></td><br><label>"
message4="<tr><td><label> Rating &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label><input type="+"text"+" name="+"rate"+"></tr></td><br>"
message5="<tr><td><label align="+"right"+">Rate 1(Lowest) to 5(Highest)</label></td></tr>"
message6="<tr><td><input type="+"submit"+" value="+"Submit"+"></tr></td></table></form></div>"
message=message1+message2+message3+message4+message5+message6;





app=Flask(__name__)
@app.route('/', methods=['GET'])
def hello_world():
    return message;


@app.route('/insertintodb', methods=['GET'])
def get_data():
	row=" "
	conn = sqlite3.connect("professor.sqlite") #create connection to zoo.sqlite database, creates the database if it doesn't already exist
	cursor = conn.cursor() #provides are cursor to the above connection (the means of executing the SQL queries)
	cursor.execute("create table if not exists professors (name text,school text, rating integer)");
	professorquery = request.args.get('professor', '').upper()
	Schoolquery = request.args.get('School', '').upper()
	ratequery = request.args.get('rate', '')
	cursor.execute("insert into professors(name, school,rating) values(?,?,?)",(professorquery,Schoolquery,ratequery))
	cursor.execute("SELECT AVG(rating)FROM professors WHERE name='"+professorquery+"' AND school = '"+Schoolquery+"'");
	data = cursor.fetchone();

	
	m1="<html><head><meta charset="+"UTF-8"+"><title>Professor rating</title></head><body  bgcolor="+"#CEF6F5"+"><hr/><h1 bgcolor="+"#CEF6F5"+" align="+"center"+">RATE MY PROFESSOR</h1>"
	m2="<hr/><div align="+"center"+"><table><tr><td><label><strong>Professor</strong> &nbsp;&nbsp;&nbsp;&nbsp;	:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label><label id="+"professor"+">"+professorquery+"</label>"
	m3="<tr><td><label><strong>School</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label><label id="+"School"+">"+Schoolquery+"</label></tr></td><br>"
	m4="<tr><td><label align="+"right"+"><strong>Average Rating</strong>&nbsp; : &nbsp;</label><label id="+"Rating"+">"+str(data).strip("(,)")+"</label></td></tr><br>"
	m5="</table></div></body></html>";
	m=m1+m2+m3+m4+m5;
	conn.commit() 
	conn.close()
	return m;
app.run(debug = True)
