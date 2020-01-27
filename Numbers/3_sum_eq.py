#given an array [ -2, -1, 0, 1, 2 ] find all triplet for which the sum results to 0
# sort the array
# maintain 3 pointers i , Left = i + 1, Right = arr.length - 1
# find the sum
# for each sum i + L + R  = sum
# if sum = 0 then iterate L++ and R--
# if sum < 0 then L++ leave right as is since we have sorted
# if sum > 0 then R-- leave left as is
# check if triplets are unique or not
# A1 iterate only until Left and Right index are same in value
# A2, A3 check whether numbers are unique triplets each time
# A5 no need to consider i when num[i] > 0 as all to nums to right of it will be greater then 0 since we sorted it

class Solution(object):

    def sum__eq(self, nums):
        ans = []
        nums.sort()
        length = len(nums)

        for i in range(length - 2):
            if nums[i] > 0: #A5
                break
            if i > 0 and nums[i] == nums[i+1]:
                continue
            L = i + 1
            R = length - 1

            while L < R: #A1
                total = nums[i] + nums[L] + nums[R]

                if total > 0:
                    R = R - 1
                elif total < 0:
                    L = L + 1
                else:
                    ans.append([nums[i], nums[L], nums[R]])

                    while L < R and nums[L] == nums[L+1]: #A2
                        L = L + 1
                    while L < R and nums[R] == nums[R-1]: #A3
                        R = R - 1
                    L = L + 1
                    R = R - 1
        return ans

    sum__eq(object, [-1,0,1,2,3,-4,-2])