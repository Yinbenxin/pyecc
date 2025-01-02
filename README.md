# py_ecc

[![Python versions](https://img.shields.io/pypi/pyversions/py-ecc.svg)](https://pypi.python.org/pypi/py-ecc)

Elliptic curve crypto in python including sm2, secp256k1, alt_bn128, and bls12_381.



## Installation

```sh
pip install .
```



#### 其中打点方式参考

```
test/hash2curve.py
```



#### PSI方式参考

```
test/hash2curve.py
```



#### 测试效果：

| 机器           | MacBook Pro : 2 GHz 四核Intel Core i5 16GB |
| -------------- | ------------------------------------------ |
| hash2curve次数 | 平均2次                                    |
| hash2curve速度 | 0.2ms/次                                   |
| 点乘速度       | 0.4ms/次                                   |
| 点除速度       | 2.6ms/次                                   |



#### 主要参考：

[py_ecc](https://github.com/ethereum/py_ecc)

[sm2](https://oscca.gov.cn/sca/xxgk/2010-12/17/1002386/files/b965ce832cc34bc191cb1cde446b860d.pdf)