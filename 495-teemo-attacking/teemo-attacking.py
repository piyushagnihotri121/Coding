class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        
        total = 0
        
        for i in range(len(timeSeries) - 1):
            # Add the minimum of duration or gap until next attack
            total += min(timeSeries[i + 1] - timeSeries[i], duration)
        
        # Add the last attack's full duration
        total += duration
        
        return total