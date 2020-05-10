'''
There are N people on a street (numbered 1 through N). For simplicity, we'll view them as points on a line. For each valid i, the position of the i-th person is Xi.

It turns out that exactly one of these people is infected with the virus COVID-19, but we do not know which one. The virus will spread from an infected person to a non-infected person whenever the distance between them is at most 2. If we wait long enough, a specific set of people (depending on the person that was infected initially) will become infected; let's call the size of this set the final number of infected people.

Your task is to find the smallest and largest value of the final number of infected people, i.e. this number in the best and in the worst possible scenario.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N.
The second line contains N space-seperated integers X1,X2,…,XN.
Output
For each test case, print a single line containing two space-separated integers ― the minimum and maximum possible final number of infected people.

Constraints
1≤T≤2,000
2≤N≤8
0≤Xi≤10 for each valid i
X1<X2<…<XN
Subtasks
Subtask #1 (10 points): N≤3
Subtask #2 (90 points): original constraints

Example Input
3
2
3 6
3
1 3 5
5
1 2 5 6 7
Example Output
1 1
3 3
2 3
'''


# cook your dish here
for _ in range(int(input())):
    test_cases = int(input())
    person = list(map(int, input().split()))
    infect_list = []
    for i in range(test_cases):
        if i==0:
            distance=0
            j=i
            infect_count = 1
            while distance<=2 and j<test_cases-1:
                distance = abs(person[j] - person[j+1])
                j+=1
                if distance <= 2:
                    infect_count += 1
            infect_list.append(infect_count)
        elif i>0 and i <= test_cases-2:
            distance=0
            j = i
            k=i
            infect_count1 = 1
            infect_count2 = 0
            while distance<=2 and j<test_cases-1:
                distance = abs(person[j] - person[j+1])
                j+=1
                if distance <=2:
                    infect_count1 += 1
            distance=0
            while distance<=2 and k>0:
                distance = abs(person[k-1] - person[k])
                k-=1
                if distance <=2:
                    infect_count2 += 1
            infect_count = infect_count1+infect_count2
            infect_list.append(infect_count)
        else:
            distance=0
            j=i
            infect_count = 1
            while distance<=2 and j>0:
                distance = abs(person[j] - person[j-1])
                j-=1
                if distance <=2:
                    infect_count += 1
            infect_list.append(infect_count)
    print (min(infect_list), max(infect_list))