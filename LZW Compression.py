# LZW Compression

def compress(uncompressed):
    """Compress a string to a list of output symbols. """
    # Build the dictionary
    dict_size = 256
    dictionary = {chr(i) : chr(i) for i in range(dict_size)}
    # dictionary = {chr(i): chr(i) for i in range(0,255)}

    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc

        else:
            result.append(dictionary[w])
            # Add wc to the dictionary
            dictionary[wc] = dict_size

            dict_size += 1
            w = c

    # Output the code for w.
    if w:
        result.append(dictionary[w])

    return result


def decompress(compressed):
    """Decompress a list of output ks to a string. """
    # Build the dictionary
    dict_size = 256
    dictionary = {chr(i) : chr(i) for i in range(dict_size)}
    # dictionary = {chr(i): chr(i) for i in range(0,255)}

    w = result = compressed.pop(0)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
            # print(entry,result)
        else:
            raise ValueError('Bad compressed k : %s' % k)
        result += entry

        # Add w + entry[0] to the dictionary.
        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry
    return result

compressed = compress("TOBEORNOTTOBEORTOBEORNOT")
print(compressed)
decompressed = decompress(compressed)
print(decompressed)
