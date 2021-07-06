import matplotlib.image as mpimg
import matplotlib.pyplot as plt


def translate(code):
	if True:
			if code == " ":
				return " "
			elif code == ".-":
				return "a"
			elif code == "-...":
				return "b"	
			elif code == "-.-.":
				return "c"
			elif code == "-..":
				return "d"
			elif code == ".":
				return "e"
			elif code == "..-.":
				return "f"
			elif code == "--.":
				return "g"
			elif code == ".....":
				return "h"	
			elif code == "..":
				return "i"
			elif code == ".---":
				return "j"
			elif code == "-.-":
				return "k"	
			elif code == ".-..":
				return "l"
			elif code == "--":
				return "m"
			elif code == "-.":
				return "n"	
			elif code == "---":
				return "o"
			elif code == ".--.":
				return "p"
			elif code == "--.-":
				return "q"
			elif code == ".-.":
				return "r"
			elif code == "...":
				return "s"
			elif code == "-":
				return "t"
			elif code == "..-":
				return "u"
			elif code == "...-":
				return "v"
			elif code == ".--":
				return "w"
			elif code == "-..-":
				return "x"
			elif code == "-.--":
				return "y"
			elif code == "--..":
				return "z"
			elif code == "-----":
				return "0"
			elif code == ".----":
				return "1"
			elif code == "..---":
				return "2"	
			elif code == "...--":
				return "3"
			elif code == "....-":
				return "4"
			elif code == ".....":
				return "5"	
			elif code == "-....":
				print("Entrou no 6")
				return "6"	
			elif code == "--...":
				return "7"
			elif code == "---..":
				return "8"
			elif code == "----.":
				return "9"					
			else:
				return ""



	
  
# Read Images
img = mpimg.imread('PNG.png')
finalcodes=[]
diff=0
for row in img:
	for col in row:
		if col[0] !=0:
			finalcodes.append(diff)
			diff=1
		else:	
			diff=diff+1
# Output Images
finalStr=""
codes =""
for c in finalcodes:
	finalStr = finalStr+chr(c)
	codes=codes +" "+ str(c)	
	
print(finalStr)	
print(codes)

translation=""
for code in finalStr.rsplit(" "):
	print(code)
	le = translate(code)
	print(" a " +le+ " a ")
	translation =translation + le
print(translation)	

