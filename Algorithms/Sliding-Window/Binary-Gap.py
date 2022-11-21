'''

Looking for longest sequence of 0s, which MUST HAVE A 1 EITHER SIDE
 e.g for 2e9 = 1110111001101011001010000000000, we return 2 (the 7th and 8th, or 16th and 17th indices)
(NOTE: the last 10 zeros are not properly surrounded by a 1, so are not a binary gap)


def BG(N):
    
    
    # display binary representation 
    bin = format(N, "b")

    maxGap = 0
    print(bin)
    l, r = 0, 0
    gap = 0
    
    while r < len(bin):
    
        if bin[r] == '1':
            l = r+1
            r = l
            maxGap = max(gap, maxGap)
            gap = 0
       
       else:
            r += 1
            gap += 1
            
            
    return maxGap   
