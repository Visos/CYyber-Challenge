


flag  = "TTZK"
ciphertext = 'Xrzlj_Alczlj_Trvjri'

'''for i in range (0, 57):
    print()'''
for j in range (0,len(flag)):
    a = ord(flag[j])+9
    if(a>122):
        print(chr((a%122)+65))
    else:
        print(chr(a), end='')
        