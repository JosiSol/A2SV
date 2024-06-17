class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        def helper(row):
            if len(row) == rowIndex + 1:
                return row
            next = [1]  

            
            for i in range(1, len(row)):
                next.append(row[i - 1] + row[i])
            
            next.append(1)  
            return helper(next)
        return helper([1])



        
        
