'''

Given a string s, replace all instances of '?', subject to constraint that there are NO 3 ADJACENT a/b CHARACTERS.
Return a list of all possible outcomes

E.g.  if s = 'aa???' we should return ['aabaa', 'aabab', 'aabba']
E.g. if s = '' we should return ['bbababa']

'''

def is_valid(state):
    return 'aaa' not in state and 'bbb' not in state

def get_candidates(state, i):
    cands = []
    add_a = state
    add_a = add_a[:i]+'a'+add_a[i+1:]
    add_b = state
    add_b = add_b[:i]+'b'+add_b[i+1:]
    if is_valid(add_a):
        cands.append(add_a)
    if is_valid(add_b):
        cands.append(add_b)
    return cands

def search(state, solutions, i):
    
    if i == len(state):
        solutions.append(state)
        return solutions
    
    if state[i] != '?':
        return search(state, solutions, i+1)
    
    
    for candidate in get_candidates(state, i):
        orig = state
        state = candidate
        search(state, solutions, i+1)
        state = orig

def solve(s):
    solutions = []
    state = s
    search(state, solutions, 0)
    return solutions
