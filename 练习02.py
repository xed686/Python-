# 題目：組合總和 II（Combination Sum II）
# 給你一個整數陣列 candidates 和一個目標值 target，
# 請找出 candidates 中所有不同的組合，讓它們加起來正好等於 target。
# 限制條件：
# •  每一個數字只能使用一次（不像經典的 Combination Sum 可以重複使用）
# •  組合中的數字必須非遞減順序（也就是排序後的樣子，例如 [1,2,2] 可以，但 [2,1,2] 不算不同的）
# •  答案中不能有重複的組合
# candidates = [10,1,2,7,6,1,5]
# target = 8
#
# [
#   [1,1,6],
#   [1,2,5],
#   [1,7],
#   [2,6]
# ]


def waicneg(c_candidates:list[int],c_target:int):
    c_candidates.sort()
    candidates=[]
    for i in c_candidates:
        if i <= c_target:
            candidates.append(i)
    parts = [] #用于存放所有合法列表
    def backtrack(num:int,remain:int,line_parts:list[int]):
        """

        :param num:当前索引
        :param remain: 还差多少数
        :param line_parts: 当前的列表
        :return:
        """
        if remain == 0:
            parts.append(line_parts[:])
            return

        for i in range(num,len(candidates)):
            if candidates[i] > remain:
                break
            if i > num and candidates[i] == candidates[i - 1]:
                continue

            line_parts.append(candidates[i])

            backtrack(i+1,remain-candidates[i],line_parts)

            line_parts.pop()


    backtrack(0,c_target,[])
    return parts

def jieshou(jieshou,mubiao):#用于接收所输入的数据
    """
    该函数主要用于将外界输入的数转换为列表 以便可以更好的带入waiceng函数
    :param jieshou:主要用于将用户输入的数转化为列表
    :param mubiao: 用于存储目标数据
    :return: 返回waiceng()
    """
    c_jieshou = [int(i) for i in candidates]
    return waicneg(c_jieshou,mubiao)

candidates = input("请你输入一串数字:")
target = int(input("请你输入你要组合的数:"))
print("你获得的组合如下：")
for i in jieshou(candidates,target): #将每个结果换行输出
    print(i)


