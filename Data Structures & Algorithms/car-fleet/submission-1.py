class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        for index in range(len(speed)):
            timeTaken=(target-position[index])/speed[index]
            pair.append([position[index],timeTaken])
        
        pair.sort(reverse=True)
        bucket=0
        minTime = 0
        for pos, timeRemaining in pair:
            if bucket==0:
                minTime=timeRemaining
                bucket+=1
            if(minTime<timeRemaining):
                minTime=timeRemaining
                bucket+=1
        return(bucket)