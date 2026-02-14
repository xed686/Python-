# 按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
# n皇后问题研究的是如何将n个皇后放置在n*k的棋盘上，并且使皇后彼此之间不能相互攻击。
# 给你一个整数n ，返回所有不同的n
# 皇后问题
# 的解决方案。
# 每一种解法包含一个不同的
# n
# 皇后问题
# 的棋子放置方案，该方案中
# 'Q'和'__'
# 分别代表了皇后和空位。
# 1 <= n <= 9 and 1 <= k <= 9
def jieshou(row, column):
    c_nums = []
    path = []#存放合法子集
    for i in range(row):
        nums = ["__"] * column #初始化棋盘
        c_nums.append(nums[:])

    def backtrack(rows):
        if rows == row:
            path.append([row[:] for row in c_nums])#必须深拷贝不能浅拷贝 否则生成的是空棋盘
            return
        for i in range(column):

            def decide(c_column): #c_column就是当前循环的i
                for n in range(column):
                    if c_nums[rows][n] == "Q":
                        return False #如果当前一行有存在皇后的话 返回False
                for n in range(row):
                    if c_nums[n][c_column] == "Q":
                        return False #如果当前一列有存在皇后的话  返回False
                #检查对角线45度和135度是否有放皇后
                n = rows - 1
                c = c_column - 1
                while n >= 0 and c >= 0:
                    if c_nums[n][c] == "Q":
                        return False #检查45度角是否存在皇后
                    n -= 1
                    c -= 1
                n = rows - 1
                c = c_column + 1
                while n >= 0 and c < column:
                    if c_nums[n][c] == "Q":
                        return False
                    n -= 1
                    c += 1
                return True

            c_column = i
            if decide(c_column):#因为在内层的函数在引用了循环中的i后在递归时便绑定了外层递归函数的i 并不会在递归遇到新的for
                                #循环时进行迭代更新 如在外层i=1 在递归后用的还是上一层的i 解决办法便是将i给赋给一个能更新的值
                c_nums[rows][i] = "Q"
                backtrack(rows+1)
                c_nums[rows][i] = "__" #回溯
    backtrack(0)
    return path

#准备输出
n = int(input("请输入行数： "))
k = int(input("请输入列数： "))
l = jieshou(n,k)
if 0 < n <=9 and 0 < k <=9:
    print(f"一共找到了{len(l)}种方案\n")
    print("你得到的组合如下： ")
    for i , fangan in enumerate(l,1):
        print(f"第{i}种方案")
        for n in fangan:
            print(n)
            print()
else:
    print("你的输入无效 请重新输入")