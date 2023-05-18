#lzss
def compress(s):
    res=""
    window=""*6
    i=0
    while i<len(s):
        ln=0
        idx=0
        for j in range(i+1,len(s)+1):         
            curr =s[i:j]
            if curr in window:
                idx=window.find(curr)
                ln=len(curr)
        if ln==0:
            res+="0" +s[i]
            window+=s[i]
            i=i+1
        else:
            res+="1(" +str(idx+1)+","+str(ln) +")"
            window +=s[i:i+ln]
            i=i+ln
        window =window[-6:]
    return res
def decompress(s):
    res=""
    window=""*6
    i=0
    while i<len(s):
        if s[i]=='0':
            res +=s[i+1]
            i=i+2
        else:
            endinx=s.find(')',i+1)
            curr=s[i+2:endinx]
            idx,ln=curr.split(',')
            idx=int(idx)
            ln=int(ln)
            seq=window[idx-1:idx-1+ln]
            res+=seq
            i=endinx+1
            window=window[-6:]
    return res
            
s=input("enter statement")
print("string before compression",s)
c=compress(s)
print("string after compression",c)
d=decompress(c)
print("string before compression",d)