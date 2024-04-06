class Solution:
   def dividePlayers(self, skill: List[int]) -> int:
       l = 0
       r = len(skill) - 1
       skill.sort()
       check_sum = skill[0] + skill[-1]
       res = 0
       while l < r:
           if skill[l] + skill[r] == check_sum:
               res += (skill[l] * skill[r])
               l += 1
               r -= 1
           else:
               return -1
       return res
