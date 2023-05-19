def compress(s):
    res = ""
    #create an empty sliding window with fixed length
    window =" "*6
    i = 0
    while i<len(s):
        #ln stores the length of the longest sequence found in window
        ln = 0
        #idx stores the index of the sequence
        idx = 0
        #search for longest sequence in window
        for j in range(i+1,len(s)+1):
            curr = s[i:j]
            if curr in window:
                idx = window.find(curr)
                ln = len(curr)
        #no sequence found in window
        if ln == 0:
            #'0' means not encoded
            res += "0" + s[i]
            #add the character to window
            window += s[i]
            i = i+1
        #a sequence was found sequence in window
        else:
            #'1' means encoded
            res += "1(" + str(idx+1) + "," + str(ln) + ")"
            #add the found string to window
            window += s[i:i+ln]
            i = i+ln
        #only keep the last 6 (fixed) characters in window
        window = window[-6:]
        
    return res
def decompress(s):
    res = ""
    window = " "*6
    i = 0
    while i<len(s):
        #'0' means a normal character, add it to result and update window
        if s[i] == '0':
            res += s[i+1]
            window += s[i+1]
            i = i + 2
        #'1' means the next characters are encoded
        else:
            # 1(start,length)
            # find start (idx), and length (ln)
            # we will search for ')' ,then from (...,..) 
            # we can determine idx,ln
            endidx = s.find(')',i+1)
            curr = s[i+2 : endidx]
            idx,ln = curr.split(',')
            idx = int(idx)
            ln = int(ln)
            #add the sequence of length ln and of index idx to result
            seq= window[idx-1:idx-1+ln]
            res+=seq
            #add the sequence to the end of window, then resize window to fixed length 6
            window += seq
            i = endidx+1
        window = window[-6:]
    return res

s=raw_input()
c = compress(s)
print(c)
d = decompress(c)
print(d)
