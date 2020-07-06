import bisect

with open('ip1.txt', 'r') as file1:
    list1 = [line.rstrip('\n') for line in file1.readlines()]
with open('ip2.txt', 'r') as file2:
    list2 = [line.rstrip('\n') for line in file2.readlines()]
    
list2.sort()
same_ip = []
"""
bisect_left(list, num, beg, end) :- This function returns the position in the sorted list, where the number passed in argument can be placed so as to maintain the resultant list in sorted order. If the element is already present in the list, the left most position where element has to be inserted is returned
"""
for i in list1:
    position = bisect.bisect_left(list2,i)
    if position < len(list2) and list2[position]==i:
        same_ip.append(i)

same_ip = list(set(same_ip)) #get unique ips and remove duplicates
print(same_ip)
        