#find: searches string for specified value, returns position of where it was found
def longestCommonPrefix(strs):

    first_str = strs [0]
    lenStrs = len (strs)
    lenChars = len (first_str)
    ans = ""
    if lenStrs == 1:
        return(first_str)
    elif lenChars == 0:
        return(ans)
    else:
        for i in range (0,lenChars):
            charToCompare = first_str [0:(i+1)]
            allSame = True
            for j in range (1, lenStrs):
                if (strs[j].find(charToCompare) != 0):
                    allSame = False
            if allSame:
                ans += charToCompare[i]
            else:
                return (ans)
    return (ans)

stt = ["car","car","car"]
print(longestCommonPrefix(stt))              

