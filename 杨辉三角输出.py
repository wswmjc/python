# coding=utf-8
def triangles(max):
    c, n = [1], 1
    while n <= max:
        print(c)
        c = [1]+[c[i-1]+c[i] for i in range(1, len(c))]+[1]
        n += 1


def main():
    while True:
        cmd = raw_input("输入杨辉三角数字？")
        if cmd == 'q':
            return
        else:
            num = int(cmd)
            triangles(num)


if __name__ == '__main__':
    main()
