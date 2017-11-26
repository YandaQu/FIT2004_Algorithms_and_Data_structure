def bwt_reverse(last_column, rank):
    row = 0
    ori = "$"
    for k in range(len(last_column) - 1):
        c = last_column[row][0]
        ori = c + ori
        row = rank[ord(c)] + last_column[row][1] - 1
    ori = ori.replace("*", " ")
    ori = ori.replace("-", "\n")
    ori = ori.replace("$", "")
    print(ori)


def counting_sort(a_list):
    count_list = [[] for num in range(ord("z") + 1)]
    for item in a_list:
        count_list[ord(item)].append(item)
    new_list = []
    for group in count_list:
        for item in group:
            new_list.append(item)
    return new_list


if __name__ == "__main__":
    f = open("exam.bz2", "r")
    contain = f.readlines()
    for i in range(len(contain)):
        contain[i] = contain[i].replace("\n", "")
        contain[i] = contain[i].split(" ")
    first_column = []
    last_column = []
    for item in contain:
        for j in range(int(item[0])):
            first_column.append(item[1])
            last_column.append(item[1])
    first_column = counting_sort(first_column)
    # until this step, last column and first column are generated

    previous = "$"
    rank = [0] * (ord("z") + 1)
    for i in range(1, len(first_column)):
        if first_column[i] != previous:
            rank[ord(first_column[i])] = i
        previous = first_column[i]

    # until this step, rank list is generated
    num_last = [0] * (ord("z") + 1)
    for j in range(0, len(last_column)):
        num_last[ord(last_column[j])] += 1
        last_column[j] = (last_column[j], num_last[ord(last_column[j])])
    # until this step, last column is numbered
    bwt_reverse(last_column, rank)
