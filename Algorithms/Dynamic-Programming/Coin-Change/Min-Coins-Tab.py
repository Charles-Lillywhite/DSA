def coinChangeTab(coins, amount):
    
    tab = [amount+1] * (amount+1)
    tab[0] = 0

    for i in range(0, amount+1):
        for c in coins:
            if (i + c) <= amount:
                tab[i+c] = min(tab[i+c], tab[i]+1)
                
    if tab[-1] == amount + 1:
        return -1
    
    return tab[-1]
