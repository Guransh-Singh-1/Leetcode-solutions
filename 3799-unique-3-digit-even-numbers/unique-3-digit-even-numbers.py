class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        counts = [0] * 10
        for d in digits:
            counts[d] += 1

        ans = 0
        
        for num in range(100,1000,2):
            temp_counts = [0] * 10
            temp_counts[num // 100] += 1
            temp_counts[(num // 10) % 10] += 1
            temp_counts[num % 10] += 1

            possible = True
            for i in range(10):
                if temp_counts[i] > counts[i]:
                    possible = False
                    break
            
            if possible:
                ans += 1
                
        return ans