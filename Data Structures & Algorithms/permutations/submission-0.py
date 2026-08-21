class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []


        def backtrack(eles):
            if not eles:
                res.append(perm.copy())
                return
           
            tempSet = set(eles)
            for ele in eles:
                tempSet.remove(ele)
                perm.append(ele)
                backtrack(tempSet)
                perm.remove(ele)
                tempSet.add(ele)
            
        backtrack(set(nums))

        return res

        