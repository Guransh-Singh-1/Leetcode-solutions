class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next

        n = len(nums)
        if n < 3:
            return [-1,-1]

        criticalpoints =[]
        for i in range(1,n-1):
            if nums[i] > nums[i - 1]  and nums[i] > nums[i+1]:
                criticalpoints.append(i)
            if nums[i] < nums[i - 1]  and nums[i] < nums[i+1]:
                criticalpoints.append(i) 
        
        if len(criticalpoints) < 2:
            return [-1,-1]
        
        maxdist = criticalpoints[-1] - criticalpoints[0]
        distances = []

        for i in range(len(criticalpoints) - 1):
            distances.append(criticalpoints[i + 1] - criticalpoints[i])

        mindist = min(distances)

        return [mindist,maxdist]