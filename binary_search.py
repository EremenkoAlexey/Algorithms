"""
При бинарном поиске искомый ключ сравнивается с ключом среднего элемента в массиве. 
Если они равны, то поиск успешен. 
В противном случае поиск осуществляется аналогично в левой или правой частях массива.
"""

def binary_search(arr: [int], key: int) -> int:
    """Looks for KEY in sorted array. Returns index of KEY or -1 if KEY was not found"""
    def search(arr: [int], start: int, end: int):
        pos = start+(end-start)//2
        if key == arr[pos]:
            return pos
        if end-start>1:
            if key > arr[pos]:
                return search(arr, pos, end)
            return search(arr, start, pos)
        return -1
    if len(arr)>0 and 0<=key<=max(arr):
        return search(sorted(arr), 0, len(arr))
    return -1

initArr = [0, 6, 1, 3, 7, 9]
KEY = 5
res = binary_search(initArr, KEY)
if res != -1:
    print("Number", KEY, "is at index", res)
else:
    print("Number", KEY, "is not in the list")
    
