"""
Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates.
 all the odd-indexed characters of S with all the even-indexed characters of S, this process should be repeated N times.

Examples:
encrypt("012345", 1)  =>  "135024"
encrypt("012345", 2)  =>  "135024"  ->  "304152"
encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

encrypt("01234", 1)  =>  "13024"
encrypt("01234", 2)  =>  "13024"  ->  "32104"
encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
Together with the encryption function, you should also implement a decryption function which reverses the process.

If the string S is an empty value or the integer N is not positive, return the first argument without changes.
"""
def Enc(text):
    even=[]
    odd=[]
    j=0
    while j<len(text):
        if(j%2==0):
            even.append(text[j])
        else:
            odd.append(text[j])
        j+=1
    enc=""
    for i in odd:
        enc+=i
    for i in even:
        enc+=i
    return enc
    
def Dec(encrypted_text):
    enc=encrypted_text
    odd=[]
    even=[]
    if(len(enc)%2==0):
        i=0
        while i<len(enc)/2:
            odd.append(enc[i])
            i+=1
        while i<len(enc):
            even.append(enc[i])
            i+=1
    else:
        i=0
        while i<len(enc)/2-1:
            odd.append(enc[i])
            i+=1
        while i<len(enc):
            even.append(enc[i])
            i+=1
        
    dec=""
    if len(enc)%2==0:
        j=0
        i=0
        while i<len(even) and j<len(odd):
            dec+=even[i]+odd[j]
            i+=1
            j+=1
    else:
        i=0
        while i<len(even):
            if i<len(odd):
               dec+=even[i]+odd[i]
            else:
                dec+=even[i]
            i+=1
        
    return dec

def decrypt(encrypted_text, n):
    if encrypted_text is None:
        return None
    dec=Dec(encrypted_text)
    i=1
    if n<=0:
        return encrypted_text
    elif n==1:
        return dec 
    else:
        while i<n:
            dec=Dec(dec)
            i+=1 
    return dec


def encrypt(text, n):
    if text is None:
        return None
    i=1
    enc=Enc(text)
    if(n<=0):
        return text
    
    elif n==1:
        return enc
    else:
        while i<n:
            enc=Enc(enc)
            i+=1
    return enc
            
print("Encryption: ",encrypt("", 0))
print(" Tah itse sits!")
print("decryption :",decrypt("hsi  etTi sats!", 1))
