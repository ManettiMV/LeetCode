class Solution:
    def maxAbsoluteSum_BRUTEFORCE(self, nums: list[int]) -> int:
        '''
        This is a brute force method with a time complexity of O(n**2)
        Basically takes a number in a list and trys to sum with every sublist possible
        and makes this for every number in the list and returns the biggest
        '''
        maxAbsSum = 0   
        EndingIndex = len(nums)
    
        for i in range(EndingIndex):
            currentSum = 0
            for j in range(i, EndingIndex):
                currentSum += nums[j]
            
                maxAbsSum = max(maxAbsSum, abs(currentSum))
        
        return maxAbsSum

    def maxAbsoluteSum_EFFICIENT(self, nums: list[int]) -> int:
        '''
        This is an efficient method with a time complexity of O(n)
        Basically looks through the sublists before the index and takes the highest and lowest
        sum of it, do the abs of the lowest and look which is bigger and returns it
        '''
        max_sum = min_sum = 0 
        current_max = current_min = 0 

        for num in nums:
            current_max = max(current_max + num, num)
            max_sum = max(max_sum, current_max)
            
            # Atualiza a soma mínima corrente
            current_min = min(current_min + num, num)
            min_sum = min(min_sum, current_min)

        return max(abs(max_sum), abs(min_sum))

example1 = [1, -3, 2, 3, -4]
example2 = [2, -5, 1, -4, 3, -2]

solut1 = Solution()
solut2 = Solution()

print(solut1.maxAbsoluteSum_BRUTEFORCE(example1))
print(solut2.maxAbsoluteSum_EFFICIENT(example2))
