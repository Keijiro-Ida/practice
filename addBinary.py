class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = 0, 0
        carry = 0
        result = []

        a = a[::-1]
        b = b[::-1]

        while i < len(a) or j < len(b) or carry:
            digit_a = int(a[i]) if i < len(a) else 0
            digit_b = int(b[j]) if j < len(b) else 0

            total = digit_a + digit_b + carry
            carry = total // 2
            result.append(str(total % 2))

            i += 1
            j += 1


        return ''.join(result[::-1])
