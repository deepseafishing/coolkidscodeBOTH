class Solution:
    def isValid(self, S: str) -> bool:
        stack = []
        valid = 'abc'
        for char in S:
            stack.append(char)
            if char == valid[len(valid) - 1]:
                if len(stack) >= 3 and valid == stack[len(stack) - 3] + stack[len(stack) - 2] + char:
                    for _ in range(len(valid)):
                        stack.pop()
                else:
                    return False


        return False if stack else True


