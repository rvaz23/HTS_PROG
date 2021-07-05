import os
import numpy as np

words=[""]*10
marked=[0]*10
#words= np.array(lista)
chars=[]#"niskyn","huzgnogo","tmhssi","dluiaca","saltet","ngasma","lepsae","sflery","osyboc","skgiin"]
wordsf= open("word.txt","r")
for f in wordsf:
	if f.rsplit("\t",1)[0] != "":
		chars.append(f.rsplit("\n",1)[0])
print(chars)

wordlist = open("wordlist.txt","r")
for line in wordlist:
	line=line.rstrip()
	for wIndex in range(len(chars)):
		if marked[wIndex] ==0:
			w=chars[wIndex]
			if len(line) == len (w):
				index=0
				good=True
				linesize = len(w)
				lineAux=line
				while index < linesize and good==True:
					aux = lineAux.find(w[index])
					if  aux != -1:
						lineAux.replace(w[index],"",1)
					else:
						good=False
					index=index+1	
				if good ==True:
					words[wIndex]=line
					#words.append(line)
					marked[wIndex] =1
	
final = words[0]
for s in range(1,len(words)):				
	final = final+ "," +words[s]
print(final)						