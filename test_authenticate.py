# to use: python authenticate.py fingerprints/jayme

from vaults import vaults
from fuzzy_vault import (unlock, decode)
from sys import argv
import warnings

known = ['jayme woogerd', 'norman ramsey', 'ming chow']

warnings.filterwarnings("ignore")


def main():
    with open("fingerprints\jayme", 'r') as f:

        # with open(argv[1], 'r') as f:  #with关键字会自动调用f.close()
        # open()返回了一个file，格式为open(filename, mode)，'r'表示只读
        # argv[1]实则指的是执行程序时使用者输入的第一个参数。
        # 直接在Spyder中运行因为没有参数传入，就会报list index out of range的错误

        #template = [float(t) for t in template]
        # 为什么要把t转换成浮点数？

        for vault in vaults:
            coeffs = unlock(template, vault)
            try:
                name = decode(coeffs)
                if name in known:
                    print('Hello, %s!' % name.title())
                    return
            except TypeError:
                pass
        print("Unknown user")


if __name__ == '__main__':
    main()

