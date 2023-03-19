# 221RDB300


def build_heap(data):
    n = len(data)
    swaps = []
    for i in range(n // 2, -1, -1):
        min_heapify(i, data, swaps)
    return swaps

def min_heapify(i, data, swaps):
    n = len(data)
    min_index = i
    left_child = 2 * i + 1
    if left_child < n and data[left_child] < data[min_index]:
        min_index = left_child
    right_child = 2 * i + 2
    if right_child < n and data[right_child] < data[min_index]:
        min_index = right_child
    if i != min_index:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        min_heapify(min_index, data, swaps)

def main():
    cmd = input()
    if "F" in cmd:
        file_path = input()
        path = "tests/"+file_path
        text = open(path)
        text1 = text.read()
        text.close()
        sep = text1.partition("\n")
        n = int(sep[0])
        data = sep[2].split(" ")
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        for i, j in swaps:
            print(i, j)



    elif "I" in cmd:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        for i, j in swaps:
            print(i, j) 

if __name__ == "__main__":
    main()       