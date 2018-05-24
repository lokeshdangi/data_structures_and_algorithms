from random import sample


array = sample(range(100),50)
array = sorted(array)[::-1]
length = len(array)

element = int(input("Enter element to be searched :"))

low = 0
high = length-1
flag = 0

while high >= low:
    mid = int((low + high)/2)
    if array[mid] == element:
        print("Element found at {} position".format(mid + 1))
        flag = 1
        break
    elif array[mid] < element:
        high = mid - 1
        print(array[low:high +1])
    elif array[mid] > element:
        low = mid + 1
        print(array[low:high + 1])

if flag == 0:
    print("Element not found")
    
    
    
    