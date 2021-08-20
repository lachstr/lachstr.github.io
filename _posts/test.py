def getIdealNums(low, high):
    # Write your code here
    
    ideal_ints = []
    
    for x in range(0, 2*10**9//3):
        for y in range(0, 2*10**9//5):
            if (3**x * 5**y) >= low:
                ideal_ints.append(3**x * 5**y)
            elif (3**x * 5**y) > high:
                return len(ideal_ints)
 
 getIdealNums(1, 1);

