def permutations(nums):
    
    def search(state, solutions):

        
        if len(state) == len(nums):
            solutions.append(state.copy())
            return solutions
        

        for i in range(0, len(nums)):
            
            if nums[i] in state:
                continue
            else:
                state.append(nums[i])
                search(state, solutions)
                state.pop()
        
            

    def solve():
        solutions = []
        state = []
        search(state, solutions)
        return solutions


    return solve()
