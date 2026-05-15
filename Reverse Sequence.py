#first iteratation, need to optimise
def reverse_seq(n):
    l = []
    for i in range(1,n+1):
        l.append(i)
        l.sort(reverse=True)
    return l

#Second iteration, still not optimal
def reverse_seq(n):
    l = []
    for i in range(1, n+1):
        l.insert(0,i)
    return l

# 3rd iteration, optimal solution, submission accepted
def reverse_seq(n):
    l=[]
    for i in range(n,0,-1):
        l.append(i)   
    return(l)

# 4th iteration, most optimal, popular solution in code wars
def reverse_seq(n):
    return list(range(n,0,-1))