import re
from asyncio.windows_events import NULL
f = open("out.txt", "w")
condon_len = 3
test= "TCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG"
dna_map = {
    "TTT":"F", "TCT":"S", "TAT":"Y", "TGT":"C", 
"TTC":"F", "TCC":"S", "TAC":"Y", "TGC":"C", 
"TTA":"L", "TCA":"S", "TAA":"STOP", "TGA":"STOP", 
"TTG":"L", "TCG":"S", "TAG":"STOP", "TGG":"W", 
"CTT":"L", "CCT":"P", "CAT":"H", "CGT":"R", 
"CTC":"L", "CCC":"P", "CAC":"H", "CGC":"R", 
"CTA":"L", "CCA":"P", "CAA":"Q", "CGA":"R", 
"CTG":"L", "CCG":"P", "CAG":"Q", "CGG":"R", 
"ATT":"I", "ACT":"T", "AAT":"N", "AGT":"S", 
"ATC":"I", "ACC":"T", "AAC":"N", "AGC":"S", 
"ATA":"I", "ACA":"T", "AAA":"K", "AGA":"R", 
"ATG":"M", "ACG":"T", "AAG":"K", "AGG":"R", 
"GTT":"V", "GCT":"A", "GAT":"D", "GGT":"G", 
"GTC":"V", "GCC":"A", "GAC":"D", "GGC":"G", 
"GTA":"V", "GCA":"A", "GAA":"E", "GGA":"G", 
"GTG":"V", "GCG":"A", "GAG":"E", "GGG":"G"
}

def GetAA(condon):
    return dna_map[condon]

class Sequence:
    def __init__(self, name, seq):
        self.name = name
        self.seq = seq
        self.found = []
    def p(self):
        print("seq name:" + self.name + "len:" + str(len(self.seq))) 
        print("seq:" + self.seq)
        for s in self.found:
            print(s) 
    def pAA(self):
        print (self.found[0])  
        f.write(self.found[0])      
    def Translate(self):
        seq_len = len(self.seq)
        aa_seq=""
        start_pos = 0
        end_pos = condon_len
        while end_pos <= seq_len:
            condon = self.seq[start_pos:end_pos]
            AA = GetAA(condon)
            if AA=="STOP":
                break
            aa_seq = aa_seq + AA
            start_pos = start_pos + condon_len
            end_pos = end_pos + condon_len
        self.found.append(aa_seq)    
        

input_file = open("rosalind_splc.txt", "r")
lines =  input_file.readlines()
list = []
s = NULL
for l in lines:
    if (l[0]==">"):
        if s != NULL:
            list.append(s)
        s = Sequence(l.replace('\n', ''), '')
    else:
        s.seq = s.seq + l.replace('\n', '')
list.append(s)        

list_len = len(list)
for i in range(1, list_len):
    list[0].seq = list[0].seq.replace(list[i].seq, '')
list[0].Translate()
list[0].pAA()    
f.close()     
