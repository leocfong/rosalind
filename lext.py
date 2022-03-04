f = open("out.txt", "w")
input_file = open("rosalind_lexf.txt", "r")
lines =  input_file.readlines()
char_array = lines[0].replace('\n', '').split(' ')
seq_len = int(lines[1])
char_array.sort()
char_array_len = len(char_array)

rep_len = []
rep_inc_counter = []
rep_char_index = []
rep_len_i = 1
for i in range(seq_len):
    rep_inc_counter.append(0)
    rep_char_index.append(0)
    rep_len.append(rep_len_i)
    rep_len_i = rep_len_i * char_array_len

num_combination = char_array_len ** seq_len
C = []

for i in range(num_combination):
    s = ""
    
    for l in range(seq_len): 
        s = char_array[rep_char_index[l]] + s

        rep_inc_counter[l] = rep_inc_counter[l] + 1
        if rep_inc_counter[l] ==  rep_len[l]:
            rep_char_index[l] = rep_char_index[l] + 1
            rep_inc_counter[l] = 0 
        if rep_char_index[l]==char_array_len:
            rep_char_index[l] = 0
    C.append(s)
for s in C:
    print(s)
    f.write(s+'\n')
f.close()     