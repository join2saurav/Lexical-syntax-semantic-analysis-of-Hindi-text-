from __future__ import unicode_literals
from Tkinter import *
from tkFileDialog import *
from nltk.tree import *
import nltk
from nltk.tag import tnt
from nltk.corpus import indian
import tkFont
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


g = open('depth_27.txt', 'w')
#with open('depth_13.txt') as f:
    #lines = f.read().splitlines()
f = open('depth_13.txt','r')
for line in f.read().split("\n"):
    if line.startswith("<Sentence"):
        g.write(line)
        g.write("\n")
    else:
        train_data = indian.tagged_sents('hindi.pos')
        tnt_pos_tagger = tnt.TnT()
        tnt_pos_tagger.train(train_data)  # Training the tnt Part of speech tagger with hindi data
        t=tnt_pos_tagger.tag(nltk.word_tokenize(line))

        grammar = r"""
            NP: {<NN.*><PREP><NP>}
                {<NN.*><PRP><NP>}
                {<JJ><NP>}
                {<JJP><NN.*>}
                {<PREP><JJ><NN.*>}
                {<QF.*><JJ><NN.*>}
                {<NN.*><NP>}
                {<Q.*><NN.*>}
                {<NN.*><PREP>}
                {<PREP><NN.*>}
                {<NN><RP>}
                {<RP><NP>}
                {<INTF><NP>}
                {<Q.*><NN.*><A>}
                {<NN.*><PREP><A>}
                {<PREP><NN.*><A>}
                {<NN.*><PREP><NP><A>}
                {<JJP><NN.*><A>}
                {<PREP><JJP><NN.*><A>}
                {<JJ>?<JJP>?<NP><A>}
                {<QF.*><NN.*><A>}
                {<QF.*><JJ><NN.*><A>}
                {<NN.*><RP><A>}
                {<QF.*><NP><A>}
                {<RP><NP><A>}
                {<INTF><NP><A>}
                {<PRP><A>}
                {<NN.*><A>}
                {<NN.*><NP><A>}
                {<PRP>}
                {<NNP>}
                {<NNPC>}
                {<NNC>}
                {<NN>}
            A:  {<CC><NP>}
            VP: {<VJJ>?<VAUX|VFM><VAUX|VFM>+}
                {<RP><VP>}
                {<Q.*><VP>}
                {<V.*><VP>}
                {<RBP><VP>}
                {<JJP><VP>}
                {<NEG><VP>}
                {<NP><VP>}
                {<NP><NP><VP>}
                {<V.*><B>}
                {<RP><VP><B>}
                {<Q.*><NP><B>}
                {<V.*><VP><B>}
                {<NP><VP><B>}
                {<RBP><NP><VP><B>}
                {<JJP><VP><B>}
                {<RBP><VP><B>}
                {<NEG><VP><B>}
                {<Q.*><VP><B>}
                {<INTF><VP><B>}
                {<VJJ>?<VAUX|VFM>+}
                {<VFM>}
                {<VAUX><VAUX>}
                {<VAUX>}
                {<VJJ>}
            B:  {<CC><VP>}# Chunk verbs and their arguments
            RBP:{<RB>}
                {<INTF><RB>}
                {<INTF><QF>}
                {<RB><E>}
                {<INTF><RB><E>}
                {<INTF><QF><E>}
                {<QF><E>}
            E:  {<CC><RBP>}
            JJP:{<JJ><NEG>}
                {<INTF><JJ>}
                {<RBP><JJ>}
                {<JJ><D>}
                {<JJ><NEG><D>}
                {<INTF><JJ><D>}
                {<RBP><JJ><D>}
                {<JJ>}
            D:  {<CC><JJP>}


             """
# CLAUSE: {<NP><VP>} # Chunk NP, VP
# """
        cp = nltk.RegexpParser(grammar)

        tr = cp.parse(t)
        g.write(str(tr))
        #splitted = tr.pprint().split()




# print u' '.join(str(tr))
