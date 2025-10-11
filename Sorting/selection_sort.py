# 비효율적, 하지만 문제에서 가장 작은 수를 찾는 경우가 많음

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
            
            
    array[i], array[min_index] = array[min_index], array[i]  # 스와프
    
print(array)