"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #8 - Triangle Perimeter (triperim.py)


Author: Ainsley Ward

Difficulty Level: 5/10

Prompt: You just got your class schedule and found out Geometry is your last period, 
after Physics, PE, English, and History. You're going to be working with triangle 
perimeters everyday this week, and will not have the brain power at the end of the day 
to do all those calculations. Luckily, you're a coding wizard and decide to come up 
with a program that returns the perimeter of a triangle, given the three vertices as 
inputs. Each of the inputs will be list types, and your code will return a float. 

Test Cases:
Input: v1 = [3, 6]; v2 = [1, 2]; v3 = [8, 2];       Output = 17.875
Input: v1 = [0, -1]; v2 = [-5, 2]; v3 = [-3, -2];   Output = 13.465
Input: v1 = [0, 0]; v2 = [1, 2]; v3 = [3, 2];       Output = 7.842
"""

class Solution:
    def tri_perimeter(self,v1, v2, v3):
        
        edge1 = (v1[0]-v2[0])*(v1[0]-v2[0])+(v1[1]-v2[1])*(v1[1]-v2[1])**(1/2)
        edge2 = (v3[0]-v2[0])*(v3[0]-v2[0])+(v3[1]-v2[1])*(v3[1]-v2[1])**(1/2)
        edge3 = (v3[0]-v1[0])*(v3[0]-v1[0])+(v3[1]-v1[1])*(v3[1]-v1[1])**(1/2)

        return edge1 + edge2 + edge3

def main():
    array1 = input().split(" ")
    array2 = input().split(" ")
    array3 = input().split(" ")

    for x in range (0, len(array1)):
        array1[x] = int(array1[x])

    for x in range (0, len(array2)):
        array2[x] = int(array2[x])

    for x in range (0, len(array3)):
        array3[x] = int(array3[x])

    tc1 = Solution()
    ans = tc1.tri_perimeter(array1,array2,array3)
    ans = round(ans,3)
    print(ans)

if __name__ == "__main__":
    main()