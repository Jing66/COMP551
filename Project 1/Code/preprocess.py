#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# import thulac
import jieba
import jieba.posseg as pseg
import re
import sys
import many_stop_words
reload(sys)
sys.setdefaultencoding( "utf-8" )

f = open("corpus_final/conversation2.txt","r")
fn = open("corpus_final/conversation2_parsed.txt","r")

# for line in f.readlines():
#     words=jieba.cut(line, cut_all = False)
#     words = [w for w in words if w]
#     w = ("/").join(words)
#     l = re.sub(r"/\s|/","",w)
#     fn.write(str(w))#.encode("gb2312")
# f.close()
# fn.close()
# exit(0)

V = set()
# preprocess
text = fn.readlines()
text = [t for t in text if t.strip("\r\n")!= "/"]
# remove punctuation
text = [re.sub(ur"[+——！，。？、~@#￥%……&*（）：；《）《》“”()»〔〕-]+", "", t.decode("utf8")) for t in text]
# remove stopwords
stops = many_stop_words.get_stop_words("zh")
text_ = []
for t in text:
    t_ = t.split("/")
    q = []
    for i in t_:
        if i not in stops and i and i!="\r\n":
            q.append(i)
            if i not in V:
                V.add(i)
    text_.append(q)
text_ = [("/").join(t) for t in text_ if t]
print(len(V))
fp = open("corpus_final/conversation2_words_nonstop.txt","w")
fp.write(("").join(text_))