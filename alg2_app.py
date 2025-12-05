# alg2_app.py - 算法二实现
import random
from sympy import prime


class Algorithm2:
    """算法二：动态进制格雷码变换"""

    def __init__(self):
        self.POOL = [3, 11, 5, 2, 7]

    def generate_bases_and_transform(self, n, mode='decode'):
        """根据输入的数字动态生成进制列表并进行编解码"""
        bases = []
        digits = []

        if mode == 'decode':
            temp = n
            seg_index = 1

            while temp > 0:
                rng = random.Random(seg_index ** 3 + prime(prime(seg_index)) + int(2 ** seg_index ** 0.5))
                shuffled_pool = self.POOL.copy()
                rng.shuffle(shuffled_pool)

                for i in range(len(shuffled_pool) - 1, -1, -1):
                    base = shuffled_pool[i]
                    remainder = temp % base
                    temp = temp // base

                    digits.append(remainder)
                    bases.append(base)

                    if temp == 0:
                        break

                seg_index += 1

            digits.reverse()
            bases.reverse()

            original_digits = [digits[0]]
            for i in range(1, len(digits)):
                original_val = (digits[i] + original_digits[i - 1]) % bases[i]
                original_digits.append(original_val)

            result = 0
            for digit, base in zip(original_digits, bases):
                result = result * base + digit

            return result

        elif mode == 'encode':
            original_num = n
            seg_index = 1

            while original_num > 0:
                rng = random.Random(seg_index ** 3 + prime(prime(seg_index)) + int(2 ** seg_index ** 0.5))
                shuffled_pool = self.POOL.copy()
                rng.shuffle(shuffled_pool)

                for i in range(len(shuffled_pool) - 1, -1, -1):
                    base = shuffled_pool[i]
                    remainder = original_num % base
                    original_num = original_num // base

                    digits.append(remainder)
                    bases.append(base)

                    if original_num == 0:
                        break

                seg_index += 1

            digits.reverse()
            bases.reverse()

            gray_digits = [digits[0]]
            for i in range(1, len(digits)):
                gray_val = (digits[i] - digits[i - 1]) % bases[i]
                gray_digits.append(gray_val)

            result = 0
            for digit, base in zip(gray_digits, bases):
                result = result * base + digit

            return result

    def encode_transform(self, n):
        """编码(正变换)"""
        if n <= 0:
            raise ValueError('n必须为正整数')
        return self.generate_bases_and_transform(n, 'encode')

    def decode_transform(self, n):
        """解码(逆变换)"""
        if n <= 0:
            raise ValueError('n必须为正整数')
        return self.generate_bases_and_transform(n, 'decode')