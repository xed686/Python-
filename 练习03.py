# 给你一个整数数组 nums，其中可能包含重复数字，返回该数组所有可能的子集（幂集）。
# 注意：解集不能包含重复的子集。
# 示例 1
# 输入：nums = [1,2,2]
# 输出：
# [[], [1], [1,2], [1,2,2], [2], [2,2]]
# 示例 2
# 输入：nums = [0]
# 输出：[[], [0]]
# 示例 3
# 输入：nums = [1,2,3]（无重复）
# 输出：[[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
# 要求
# •  答案中子集可以按任意顺序返回
# •  但同一个子集只能出现一次（去重）
# •  nums 长度 ≤ 10，数值范围 -10 ~ 10
# 提示
# 这道题和「子集 I」几乎一样，但因为有重复数字，必须处理去重。
# 核心思路和「组合总和 II」非常像：排序 + 同一层去重 + 索引递增。


def add(c_nums:list):
    c_nums.sort()#先将输入的列表进行排序
    path = [] #用于接收所有列表组合
    def backtrack(num:int,current_path:list):
        """

        :param num:当前索引
        :param current_path:当前的列表
        :return:
        """
        path.append(current_path[:])
        for i in range(num, len(c_nums)):
            if i > num and c_nums[i] == c_nums[i-1]:
                continue
            current_path.append(c_nums[i])
            backtrack(i+1,current_path)
            current_path.pop()
            #个人理解：第1次的循环的递归会将带有第一个数的子集给全部输出 而第2次循环则会将以第二个数开头的数为第一位的子集给全部输出
    backtrack(0,[])
    return path
def zhuanhuan(c_n):
    c_nums = [int(i) for i in c_n]
    return add(c_nums)


n = input("请你输入一串数字 会将它的所有子集拆分出来")
print(f"所有子集如下{zhuanhuan(n)}")