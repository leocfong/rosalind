c_map = {
    "A":"T",
    "G":"C",
    "C":"G",
    "T":"A"
}
def GetComplement(seq):
    r = ''.join([c_map[x] for x in seq])
    return r
def GetRevComplement(seq):
    c = GetComplement(seq) 
    return c[::-1]   

f = open("out.txt", "w")
input_file = open("rosalind_revp.txt", "r")
seq = ""
lines =  input_file.readlines()
for l in lines:
    if (l[0]!=">"):
        seq = seq + l.replace("\n", "").replace("\r","")


seq_len = len(seq)

start_len = 2
end_len = 6
found_list = {}
for i in range(start_len, end_len+1): 
    for j in range(0, seq_len-(i*2)+1):
        first_half = seq[j:j+i]
        second_half =seq[j+i:j+i*2]
        rc_second_half = GetRevComplement(second_half)
        if (first_half == rc_second_half):
            #print(first_half + " " + second_half + " " + rc_second_half + " " + str(j+1) + " " +str(i*2))
            found_list[j+1]=i*2
sorted_found_list = sorted(found_list.items(), key=lambda item: item[0])
for key, value in sorted_found_list:
    print(str(key) + " " + str(value))            
    f.write(str(key) + " " + str(value) + '\n')
f.close()   