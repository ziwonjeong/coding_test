# 삽입 정렬: 특정한 데이터를 기준으로 정렬된 데이터의 위치를 찾아서 삽입하는 방식
# 삽입 정렬은 데이터가 거의 정렬되어 있을 때 매우 빠르게 동작한다.
# 삽입 정렬은 O(N^2)의 시간 복잡도를 가진다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break
            

print(array)