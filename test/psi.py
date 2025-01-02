from pyecc.sm2 import *
import time
def PSI(data_number, intersection_number):
    common = ['intersection'+str(i) for i in range(intersection_number)]
    alice_data = ['Alice'+str(i) for i in range(data_number-intersection_number)]
    bob_data = ['Bob'+str(i) for i in range(data_number-intersection_number)]
    alice_data += common
    bob_data += common

    key1 = Sm2key("alice")
    key2 = Sm2key("Bob1")
    time_start = time.time()
    # 进行PSI计算
    # 1. 双方本地计算，求交方发送给结果给辅助方
    alice_point = key1.encrypt(alice_data)
    bob_point = key2.encrypt(bob_data)
    # 2. 双方交换加密后的点，辅助方将结果发送给待求交方
    alice_point_twice=key1.encrypt_twice(bob_point)
    bob_point_twice=key2.encrypt_twice(alice_point)
    time_end = time.time()

    # 使用集合来提高查找效率
    bob_point_twice_set = set(bob_point_twice)
    # 遍历 alice_point_twice，检查是否在 bob_point_twice_set 中
    intersection = [alice_data[i] for i, point in enumerate(alice_point_twice) if point in bob_point_twice_set]

    print("PSI计算时间：", time_end - time_start)

    # 3. 本地计算比对结果
    if len(set(common) & set(intersection)) != len(common):
        return False
    else:
        return True

if __name__ == '__main__':
    intersection = PSI(1000,100)
    print("求交计算:", intersection)