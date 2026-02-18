# 力扣04
#寻找两个正序数组中的中位数
#给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
# 算法的时间复杂度应该为 O(log (m+n))
def decidedecide(num1,num2):
    """

    :param num1: 数组1 保证为最短的数组
    :param num2: 数组2
    :return: 返回中位数((max(left1, left2)+min(right1, right2))/2 或者 max(left1, left2))
    """
    if len(num1) > len(num2):
        num1, num2 = num2, num1 #确保num1为最短的数组
        m = len(num1) # m始终为短的数组长度
        n = len(num2) # n始终为长的数组长度 确保有len(m) <= len(n)
    else:
        m = len(num1)
        n = len(num2)
    #左边的元素个数
    left_total = (n+m+1)//2 #加1是为了在总长度为奇数的时候好取整
    #left1为num1的左边每次二分最小的那个数 left2则是左边部分num2最小的数
    #right1为num2的右边每次二分最小的那个数 right2则是右边部分num2最小的数
    k = 0 #用于计数循环次数
    left = 0 #sum1二分起点
    right = m #sun1二分终点
    while True: #True将导致循环一直重复 若是输入错误将导致一直处于死循环因此需要加限定条
        i = left + (left + right) // 2 #(left+right)//2 是每次二分时i所需前进的数
        j = left_total - i #因为有i+j==left_total
        if i > 0:#如果num1中右边的数小于0 则记为负无穷
            left1 = num1[i-1]
        else:
            left1 = float('-inf')
        if i < m:
            right1 = num1[i]
        else:
            right1= float('inf')
        if j > 0:
            left2 = num2[j-1]
        else:
            left2 = float('-inf')
        if j < n:
            right2 = num2[j]
        else:
            right2 = float('inf')

        if left1 <= right2 and left2 <= right1:
            if (n + m) % 2 == 0:
                return (max(left1, left2)+min(right1, right2))/2
            else:
                return max(left1, left2)
        elif left1 > right2:
            right = i-1
        else:
            left = j+1
            
        if k >20:#如果k大于20 则退出循环
            break
        
print(decidedecide([1, 3], [2]))  # 应输出 2.0
print(decidedecide([1, 3, 8, 9, 15], [7, 11, 18, 19, 21, 25]))  # 应输出 11.0

    #测试用例2：偶数总长度
print(decidedecide([1, 2], [3, 4]))  # 应输出 2.5
print(decidedecide([0, 0], [0, 0]))  # 应输出 0.0

