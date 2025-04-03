class Solution:
    def numOfSubarrays_BRUTEFORCE(self, arr: list[int]) -> int:
        '''
        This is a Bruteforce method with a time complexity of O(n^2)
        It takes an element and checks the sublists before it until it gets to itself
        doing a Sum of everything and checking if is an odd sum or not, if is it gets added
        to a result list, then for the result we just get the len of the list
        '''
        MOD = 1e9 + 7
        res = 0
        arr_len = len(arr)
        for i in range(arr_len):
            currentSum = 0
            for j in range(i,arr_len):
                currentSum+=arr[j]
                if currentSum % 2 != 0:
                    res+=1
        return int(res % MOD)
    
    def numOfSubarrays_EFFICIENT(self, arr: list[int]) -> int:
        '''
        This is an efficient method with a time complexity of O(n)
        It iterates through the array, keeping track of the cumulative sum at each index.
        It checks if the current cumulative sum is odd or even and counts how many odd or even sums have occurred so far.
        Using this count, it adds the result to the total number of odd subarrays and returns the final count modulo 10^9 + 7.
        '''
        MOD = 10**9 + 7
        odd_count = 0
        even_count = 1
        current_sum = 0
        result = 0
        
        for num in arr:
            current_sum += num
            if current_sum % 2 != 0:
                result += even_count
                odd_count += 1
            else:
                result += odd_count
                even_count += 1

            result %= MOD

        return result
        
example1 = [1,3,5]
example2 = [1,2,3,4,5,6,7]

solut1 = Solution()
solut2 = Solution()

print(solut1.numOfSubarrays_BRUTEFORCE(example1))
print(solut2.numOfSubarrays_EFFICIENT(example2))