"""
Ada and Dishes
Chef Ada is preparing N dishes (numbered 1 through N). For each valid i, it takes Ci minutes to prepare the i-th dish. The dishes can be prepared in any order.

Ada has a kitchen with two identical burners. For each valid i, to prepare the i-th dish, she puts it on one of the burners and after Ci minutes, 
removes it from this burner; the dish may not be removed from the burner before those Ci minutes pass, because otherwise it cools down and gets spoiled. 
Any two dishes may be prepared simultaneously, however, no two dishes may be on the same burner at the same time. Ada may remove a dish from a burner and 
put another dish on the same burner at the same time.

What is the minimum time needed to prepare all dishes, i.e. reach the state where all dishes are prepared?

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N.
The second line contains N space-separated integers C1,C2,…,CN.
Output
For each test case, print a single line containing one integer ― the minimum number of minutes needed to prepare all dishes.

Constraints
1≤T≤1,000
1≤N≤4
1≤Ci≤5 for each valid i
Subtasks
Subtask #1 (1 points): C1=C2=…=CN
Subtask #2 (99 points): original constraints

Example Input
3
3
2 2 2
3
1 2 3
4
2 3 4 5
Example Output
4
3
7
Explanation
Example case 1: Place the first two dishes on the burners, wait for two minutes, remove both dishes and prepare the last one on one burner.

Example case 2: Place the first and third dish on the burners. When the first dish is prepared, remove it and put the second dish on the same burner.

Example case 3: Place the third and fourth dish on the burners. When the third dish is prepared, remove it and put the second dish on the same burner. 
Similarly, replace the fourth dish (when it is prepared) by the first dish on the other burner.

"""

num_dishes=5
time_dishes=[2,3,4,5,1]
if num_dishes == 1:
    print(time_dishes[0])
else:
    time_dishes.sort(reverse=True)
    # print(time_dishes)
    burners=[]
    i=0
    time = 0
    while i<=num_dishes:
        if i==0 and len(burners)==0:
          burners.extend(time_dishes[:2])
          print(burners)
          min_time = min(burners)
          print(min_time)
          burners = [x - min_time for x in burners]
          print(burners)
          time = time+min_time
          print(time)
          burners.remove(0)
          print(burners)
          i+=2
        elif i<num_dishes and len(burners)==1:
            print('step 2')
            burners.append(time_dishes[i])
            min_time = min(burners)
            burners = [x - min_time for x in burners]
            print(burners)
            time = time+min_time
            print(time)
            burners.remove(0)
            print(burners)
            print('not empty',burners)
            print(i)
            i+=1
            print(i)
            print('num dish', num_dishes)
            #break
        elif i==num_dishes and len(burners)==1:
            time= time+burners[0]
            print('step final', time)
            i+=1
print('final time', time)

# cook your dish here
for _ in range(int(input())):
    num_dishes = int(input())
    time_dishes = list(map(int, input().split()))
    if num_dishes == 1:
        print(time_dishes[0])
    else:
        time_dishes.sort(reverse=True)
        print(time_dishes)