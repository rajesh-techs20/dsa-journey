class Solution:
  def Pattern2(self,n):
    for i in range(n):
      for j in range(i+1):
        print("*", end="")
      print()

OUTPUT
 if n = 5
*
**
***
****
*****
