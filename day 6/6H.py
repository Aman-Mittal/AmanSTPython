#filter() filters an iterable by removing items that dont match the predicate
#predicate is the function that returns a boolean
def find_odd(x):
    if x%2==1:
        return True
    else:
        return False
nums=[11,22,33,44,55]
result=list(filter(find_odd,nums))
print(nums)
print("odd",result)
print("-"*20)
num=[11,22,33,44,55]
result=list(filter(lambda x:x%2==1,num))
print("odd:",result)
print('-'*20)
result=list(filter(lambda x:x%2==0,num))
print("Even:",result)
