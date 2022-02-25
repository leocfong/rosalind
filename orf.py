import re
condon_len = 3
c_map = {
    "A":"T",
    "G":"C",
    "C":"G",
    "T":"A"
}
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

found = []
input_file = open("rosalind_orf.txt", "r")

def GetComplement(seq):
    r = ''.join([c_map[x] for x in seq])
    return r

def GetAA(condon):
    return dna_map[condon]

def GetAASeq(dna_seq, pos):
    dna_seq_len = len(dna_seq)
    seq=""
    start_pos = pos
    end_pos = pos + condon_len
    condon = dna_seq[start_pos:end_pos]
    AA = GetAA(condon)
    while AA != "STOP":
        seq = seq + AA
        start_pos = start_pos + condon_len
        end_pos = end_pos + condon_len
        if (end_pos> (dna_seq_len-1)):
            return "" #end of seq reached without finding stop condon
        condon = dna_seq[start_pos:end_pos]
        AA = GetAA(condon)
    found.append(seq)    
    return seq   
dna_seq = ""
lines =  input_file.readlines()
for l in lines:
    if (l[0]!=">"):
        dna_seq = dna_seq + l.replace("\n", "").replace("\r","")
r_dna_seq = GetComplement(dna_seq[::-1])

seq_regex="ATG"

p = re.compile(seq_regex)
for m in p.finditer(dna_seq):
    GetAASeq(dna_seq, m.start())

for m in p.finditer(r_dna_seq):
    GetAASeq(r_dna_seq, m.start())   

for s in list(set(found)):
    print(s)     

