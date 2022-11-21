def coinChangeMemo(coins, amount):
    memo = {}
    def change(c, a):
      
        if a < 0:
            return -1
        if a == 0:
            return 0
        if a in memo:
            return memo[a]
            
        fewest = amount + 1
        for i in c:
            rem = a - i
            rem_res = change(c, rem)
            if rem_res != -1:
                res = rem_res + 1
                fewest = min(fewest, res)
        if fewest <= amount:
            memo[a] = fewest
            return fewest
        memo[a] = -1
        return -1
      
    return change(coins, amount)
