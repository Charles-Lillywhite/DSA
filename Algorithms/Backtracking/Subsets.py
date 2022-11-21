'''

Generate all UNIQUE subsets of the elements in an array, including the empty subset

E.g.

subsets([1, 2, 3]) should return [ [], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3] ]

'''


def subsets(nums):
    
    def search(state, solutions, idx):

        solutions.append(state.copy())

        for i in range(idx, len(nums)):
            state.append(nums[i])
            search(state, solutions, i + 1)
            state.pop()

    def solve(idx):
        solutions = []
        state = []
        search(state, solutions, idx)
        return solutions


    return solve(0)
