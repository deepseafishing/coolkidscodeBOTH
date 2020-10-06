class Solution:
    def multiply(self, num1, num2):
        product = [0] * len(num1 + num2)
        position = len (product) - 1
        for n1 in num1[::-1]:
            temp = position
            for n2 in num2[:: -1]: # top integer
                int_n1 =ord(n1) - ord('0')
                int_n2 =ord(n2) - ord('0')
                product[temp] += int_n1 * int_n2
                product[temp - 1] += product[temp] // 10
                product[temp] %= 10
                temp -= 1
            position -= 1
        cut = 0
        while cut < len(product) - 1 and product[cut] == 0:
            cut += 1

        return ''.join(map(str, product[cut:]))


