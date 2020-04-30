class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        def _helper(acc, curr):
            if (curr not in '/+-*'):
                acc.append(int(curr))
            else:
                last = acc.pop()
                second_to_last = acc.pop()
                if(curr == '/'):
                    acc.append(int(second_to_last / last))
                elif(curr == '+'):
                    acc.append(second_to_last + last)
                elif(curr == '-'):
                    acc.append(second_to_last - last)
                else:
                    acc.append(last * second_to_last)
            return acc

        return reduce(_helper, tokens, [])[0]


# is number?
# def _helper(x, y):
#     print(x, y)
#     return x + y
# print(reduce(_helper, [1, 2, 3, 4, 5]))
