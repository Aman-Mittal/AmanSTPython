numbers={'first':1,'second':2,'third':3,'five':5}
print(numbers)
#{'first':1,'second':2'third':3,'five':5}
print(sorted(numbers))
print(sorted(numbers,reverse=True))
print(sorted(numbers.values()))
print(sorted(numbers.values(),reverse=True))
print(sorted(numbers,key=number.__getitem__))
print(sorted(numbers,key=numbers.__getitem__,reverse=True))
