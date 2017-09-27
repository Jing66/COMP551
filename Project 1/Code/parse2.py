# parse conversation
import random
import re

text = open("corpus/conversation.txt").readlines()
text = [t.strip("\n") for t in text if t != "\n"]

q1=[]
q2=[]

tt = ""

out = "<dialog>\n"

for idx in range(0,len(text),2):
	t = eval(text[idx])
	t = [i.strip("\n") for i in t if t and t!="\n"]
	txt = (";").join(t)
	t_ = txt.split(":")
	t_ = [i for i in t_ if i]
	q1.append(t_)

for idx in range(1,len(text),2):
	t = eval(text[idx])
	t = [i.strip("\n") if i!= "\n" and t else ":" for i in t ]
	txt = (";").join(t)
	t_ = txt.split(":")
	t_ = [i for i in t_ if i]
	q2.append(t_)

for q3,q4 in zip(q1,q2):
	q3 = q3[:min(len(q3),len(q4))]
	q4 = q4[:min(len(q3),len(q4))]
	stop = random.randint(0,1)
	if stop == 1:
		out += "</dialog>\n<dialog>\n"
	out_ = "<s>"
	for i,j in zip(q3,q4):
		i = re.sub("\n","",i)
		j = re.sub("\n","",j)
		out_ += '<utt uid="1">'+i.strip(";")+"</utt>"
		out_ += '<utt uid="2">'+j.strip(";")+"</utt>"
		tt += i.strip(";")+"\n"
		tt += j.strip(";")+"\n"
	out_ += "</s>\n"
	out += out_

fp = open("corpus/conversation_parsed2.xml","w")
fp.write(out)

# fp =  open("corpus/conversation_parsed_raw.txt","w")
# fp.write(tt)