s = "XI"
lenInd = len (s) -1
arr = ["I", "V", "X", "L", "C", "D", "M"]
corresValues = [1,5,10,50,100,500,1000]

# go from right to left 
currInd = 0 
ans = 0

while lenInd >= 0:
    if (lenInd == len (s) -1):
        matchingInd = arr.index(s[lenInd])
        currInd = matchingInd
        ans += corresValues[matchingInd]
    else:
        matchingInd = arr.index(s[lenInd])
        if (currInd > matchingInd):
            ans -= corresValues[matchingInd]
        else:
            currInd = matchingInd
            ans += corresValues[matchingInd]

    lenInd -= 1
print(ans)