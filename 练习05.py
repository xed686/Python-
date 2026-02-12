# 题目：有重复字符的字符串全排列
# 给定一个字符串 s，其中可能包含重复字符，请返回 所有不重复的全排列，可以按任意顺序返回。
# 要求：
# •  答案中不能包含重复的排列
# •  字符串长度 ≤ 10
# •  字符范围：小写字母 a-z 或 数字 0-9
# 示例 1
# 输入：s = “aabb”
# 输出：[“aabb”, “abab”, “abba”, “baab”, “baba”, “bbaa”]
# （共 6 种）
# 示例 2
# 输入：s = “abc”
# 输出：[“abc”,“acb”,“bac”,“bca”,“cab”,“cba”]
# （共 6 种）
# 示例 3
# 输入：s = “aaa”
# 输出：[“aaa”]
# （共 1 种）
# 示例 4
# 输入：s = “a1a”
# 输出：[“a1a”,“aa1”,“1aa”]
# （共 3 种）
def jieshou(c_nums):
    """
    首先把接收到的字符串给排列好 再将数字类型的str转化成int类型
    :param c_nums:接收到的字符串
    :return: path
    """
    c_nums.sort()
    path = []#用于存放所有合法子集
    sued = [False] * len(c_nums)

    def backtrack(c_path):
        if len(c_path) == len(c_nums):
            path.append(c_path[:])
            return

        for i in range(len(c_nums)):
            if sued[i] == True:
                continue
            if i > 0 and c_nums[i - 1] == c_nums[i] and not sued[i - 1]:
                continue
            c_path.append(c_nums[i])
            sued[i] = True
            backtrack(c_path)
            sued[i] = False
            c_path.pop()

    backtrack([])
    return path

def main(nums):
    #将输入的srt给遍历转化为列表
    c_nums = []
    for i in nums:
        c_nums.append(i)
    return jieshou(c_nums)

#输入
n = input("请你输入一串长度在10以内的字符串: ")
if len(n) > 10:
    print("输入错误请输入长度在10以内的字符串")
else:
    print("你得到的全排列如下： ")
    for i in main(n):
        print(''.join(map(str,i)))