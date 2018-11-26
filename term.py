import os
import compute
import subprocess as sub
import re
import sys
try:
	output=sys.argv[1]
	s = ""
	if(re.findall(r"py$",output)):
		s = "python3 "+output
	elif(re.findall(r"java$",output)):
		s = "javac " + output
	elif(re.findall(r"cpp$",output)):
		s = "g++ " + output
	elif(re.findall(r"c$",output)):
		s = "gcc " + output
	'''regex to understand the type of file'''
	if(s != ""):
		s1=s+" 2> a1.txt"
		k=os.system(s1)
		with open ("a1.txt","r") as f:
			s2=""
			s2=s2+f.read()
		if(len(s2)!=0):
			m=re.findall(r'.*?[eE]rror:.*',s2)
			for i in m:
				res = compute.mainFunction(i)
			'''to generate dialog box in case of error '''
		else:
			s+=" > a1.txt"
			with open("a1.txt","r") as f:
				print(f.read())
		'''execute in case of no error '''
	os.remove("a1.txt")
except Exception as e:
	print (e)
	

