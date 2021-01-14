import glob ,re
index=0
word=[]
end_L=0
start_L=127

word_len = int(input("Enter the word lenth: "))

L_type = input("Enter the somples that want 2 be used  as @ , A, a ,0: ")

if re.search(r'\d', L_type):
    if start_L > 48: start_L=48
    if end_L < 56:end_L =56

if re.search(r'[a-z]', L_type):
    if start_L > 97: start_L=97
    if end_L < 121:end_L =121

if re.search(r'[A-Z]', L_type):
    if start_L > 65: start_L=65
    if end_L < 89:end_L =89

if re.search(r'[^a-zA-Z0-9]', L_type):
    if start_L > 32: start_L=32
    if end_L < 125:end_L =125

for x in range(word_len):
    word.extend(chr(start_L))


words=glob.glob('word_list.txt')

while True:   
    for script in words:
        with open(script,'w') as f:
            f.writelines(word)
            f.writelines('\n')
         
    try:
        while ord(word[index]) > end_L:
            word[index]=chr(start_L)
            index=index+1
      
        word[index]=chr(ord( word[index])+1)
        index=0
    except:
        print("done")
        break

