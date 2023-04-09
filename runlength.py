#run length
def rle_encode(data):
    encoding=''
    prev_char=''
    count=1
    if not data: return ''
    
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding+=str(count)+prev_char
            count=1
            prev_char=char
        else:
            count+=1
    encoding += str(count)+prev_char
    return encoding
def rle_decode(data):
    decode=''
    for char in data:
        if char.isdigit():
            count=int(char)
        else:
            decode += char * count
    return decode
encoded_val=rle_encode('AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE')
print(encoded_val)
decoded_val=rle_decode('6A1F2D7C1A17E')
print(decoded_val)
        
