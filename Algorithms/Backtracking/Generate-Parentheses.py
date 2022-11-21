def generate_parentheses(n):
    
    def is_valid(state):
        return state.count('(') >= state.count(')') and state.count('(') <= n

    def get_candidates(state):
        c1 = state + '('
        c2 = state + ')'
        candidates = []
        
        if is_valid(c1):
            candidates.append('(')
        if is_valid(c2):
            candidates.append(')')
        
        return candidates

    def search(state, solutions):

        if len(state) == 2*n:
            solutions.append(state)
            
        for candidate in get_candidates(state):
            orig = state
            state += candidate
            search(state, solutions)
            state = orig

    def solve():
        solutions = []
        state = ''
        search(state, solutions)
        return solutions
        
    
    return solve()
