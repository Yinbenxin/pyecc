from hashlib import sha256
from symtable import Class

from pyecc.sm2 import sm2
import os
def hash2curve(plaint_text: str):
    # 计数器
    if not isinstance(plaint_text, bytes):
        message = plaint_text.encode('utf-8')

    counter = 0
    while True:
        # 计算 message 和 counter 的 hash
        data = message + counter.to_bytes(32, 'big')
        hash_digest = sha256(data).digest()
        # 从 hash 计算 x 坐标
        x = int.from_bytes(hash_digest, 'big') % sm2.P

        # 尝试通过椭圆曲线方程 y^2 = x^3 + ax + b,计算 y^2
        y_squared = (pow(x, 3, sm2.P) + sm2.A * x + sm2.B) % sm2.P

        # 计算 y^2 在模 p 下的平方根，如果有的话
        # 对于椭圆曲线，(y^2)^((p+1)/4) % p = y^((p+1)/2) % p=y^(1/2) * y^(p/2) % p =y
        # 费马小定理：a^(p) ≡ a mod p
        y = pow(y_squared, (sm2.P + 1) // 4, sm2.P)

        # 如果 y^2 = y_squared，说明 y^2 是二次剩余， (x, y) 是椭圆曲线上的点，返回它
        # 如果不是，则 counter 加一，再试一次
        if pow(y, 2, sm2.P) == y_squared:
            # y^2 有两个平方根 y 和 -y，我们利用 hash 的最后一位决定 y 的符号
            sign_bit = hash_digest[-1] & 1
            if sign_bit == 1:
                y = sm2.P - y  # Use -y
            return  (x, y)
        counter += 1 # 平均常数2次

def list2curve(plaints: list):
    points = [hash2curve(plain) for plain in plaints]
    return points


class Sm2key:
    def __init__(self, key):
        if key is None:
            keys = os.urandom(32)
        else:
            keys = key.encode('utf-8')
        keys = int.from_bytes(keys, 'big') % sm2.N
        self.key = keys
        self.key_inverse = pow(keys, -1, sm2.P)

    def encrypt(self, plaints: list):
        points = list2curve(plaints)
        points_enc = [sm2.multiply(i, self.key) for i in points]
        return points_enc

    def encrypt_twice(self, points: list):
        points_enc = [sm2.multiply(i, self.key) for i in points]
        return points_enc

    def decrypt(self, points: list):
        points_enc = [sm2.multiply(i, self.key_inverse) for i in points]
        return points_enc
