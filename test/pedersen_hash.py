from pyecc.secp256k1 import secp256k1
import os
from hashlib import sha256

def pedersen_hash(G, P, m, r):
    """
    利用 secp256k1 上的两个点 G 和 P 计算 Pedersen hash
    :param G: secp256k1 生成点
    :param P: 通过 hash-to-curve 生成的点
    :param m: 消息
    :param r: 随机数
    :return: The Pedersen hash as a point on the secp256k1 curve.
    """
    hash_point = secp256k1.add(secp256k1.multiply(G, m), secp256k1.multiply(P, r))
    return hash_point

def message_to_int(message):
    """将消息转换为int"""
    message_hash = sha256(message.encode('utf-8')).digest()
    return int.from_bytes(message_hash, 'big')

# 示例
G = secp256k1.G
P = (75672206050705717597513752332592681441562708170391675094677140490692301502235, 2079954378639550643990441934946533201466680551826647417569849183466717633402)
m = message_to_int('Example message')
r = int.from_bytes(os.urandom(32), 'big') % secp256k1.N  # Random blinding factor
print(f"随机数r: {r}")
# 随机数r: 73024396533133913522992000700997978493545300935845156062873113842229351634806

hash_point = pedersen_hash(G, P, m, r)
print(f"Pedersen hash: {hash_point}")

