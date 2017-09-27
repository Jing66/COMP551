# one line per utterance
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

text = open("corpus_final/conv_2.xml").read()
sub_text = re.sub('<(.*?)>',"\n",text)

sub_text = re.sub(r'(\n)+','\n',sub_text)

f = open("corpus_final/conversation2.txt","w")
f.write(sub_text)