# alg1_app.py - 算法一实现
import random


class Algorithm1:
    """算法一：固定进制格雷码变换"""

    def __init__(self):
        self.bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        random.seed(65537)
        random.shuffle(self.bases)

    def gray_base(self, n: int, base: int) -> int:
        """通用进制格雷码变换"""
        if n == 0:
            return 0

        digits = []
        temp = n
        while temp > 0:
            digits.append(temp % base)
            temp //= base

        if not digits:
            return 0

        digits.reverse()
        gray_digits = [digits[0]]
        for i in range(1, len(digits)):
            gray_digits.append((digits[i] - digits[i - 1]) % base)

        result = 0
        for digit in gray_digits:
            result = result * base + digit

        return result

    def gray_base_inv(self, g: int, base: int) -> int:
        """通用进制格雷码逆变换"""
        if g == 0:
            return 0

        digits = []
        temp = g
        while temp > 0:
            digits.append(temp % base)
            temp //= base

        if not digits:
            return 0

        digits.reverse()
        original_digits = [digits[0]]
        for i in range(1, len(digits)):
            original_digits.append((digits[i] + original_digits[i - 1]) % base)

        result = 0
        for digit in original_digits:
            result = result * base + digit

        return result

    def forward_transform(self, n):
        """正变换"""
        if n <= 0:
            raise ValueError('n必须为正整数')

        result = n
        for base in self.bases:
            result = self.gray_base(result, base)

        return result

    def inverse_transform(self, n):
        """逆变换"""
        if n <= 0:
            raise ValueError('n必须为正整数')

        result = n
        for base in reversed(self.bases):
            result = self.gray_base_inv(result, base)

        return result