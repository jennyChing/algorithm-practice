def count_inversion(li, c):
    length = len(li)
    if length < 2:
        return li
    else:
        middle = int(length / 2)
        return count_split_inversion(count_inversion(li[:middle], c), \
                                     count_inversion(li[middle:], c), c)
def count_split_inversion(left, right, c):
    result = []
    while left and right:
        curr = left if left[0] < right[0] else right
        result.append(curr.pop(0))
        if curr == right:
            c[0] += len(left)
    result.extend(left if left else right)
    return result
def main():
    count = [0]
    f = open("QuickSort.txt","r")
    line_list = f.readlines()
    int_list = [int(line.split()[0]) for line in line_list if line]
    count_inversion(int_list, count)
    print(count[0])
if __name__ == '__main__':
    main()
