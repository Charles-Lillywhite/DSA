def coinChangeBest(coins, amount):
  
    tab = [None] * (amount+1)
    tab[0] = []
    
    for i in range(0, amount+1):
        if tab[i] is not None:
            for c in coins:
                if i + c <= amount:
                    newComb = tab[i] + [c]
                    if tab[i+c] is None or len(newComb) < len(tab[i+c]):
                        tab[i+c] = newComb
                
    return tab[-1]
