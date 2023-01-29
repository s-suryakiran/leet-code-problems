class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        for i in range(0, len(numbers)):
            d[numbers[i]] = i
        ans = []
        index = 1
        for i in numbers:
            if d.get(target-i,0) !=0:
                ans.append(index)
                ans.append(d[target-i]+1)
                return ans
            index +=1