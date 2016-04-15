import os
import re

jsonoutPut = os.popen("sudo make tag").read()

cnt = 0
text_file = open("POSOut.txt", "wb")
text_file.write("<s>" + "\n")
for line in jsonoutPut.splitlines():
	if cnt <2:
		cnt+=1
		continue
	line = re.split(r'\t+', line)
	if '<s>' in line:
		text_file.write("<s>" + "\n")
	if '</s>' in line:
		text_file.write("</s>" + "\n")
	try:
		text_file.write(line[0] + " " + line[2] + "\n")
	except:
		pass
	cnt+=1
	
text_file.write("</s>" + "\n")
text_file.close()
os.popen("rm hindi.tmp.words")