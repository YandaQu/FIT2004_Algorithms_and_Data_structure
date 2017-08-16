

# this function read the file into python and store as a list
# time complexity O(MN), space complexity O(MN)
def file_oper(file_name):
    file = open(file_name, "r")
    # read file as a string
    contain = file.read()
    # convert into list by "\n"
    contain = contain.split("\n")
    return contain


# this function give signature for all the words
# time complexity O(MN), space complexity O(MN)
def give_sig_all(a_list):
    table = {"a": 2, "b": 3, "c": 5, "d": 7, "e": 11, "f": 13, "g": 17, "h": 19, "i": 23, "j": 29, "k": 31, "l": 37,
             "m": 41, "n": 43, "o": 47, "p": 53, "q": 59, "r": 61, "s": 67, "t": 71, "u": 73, "v": 79, "w": 83, "x": 89,
             "y": 91, "z": 101}
    i = 0
    # for every word, calculate the signature
    while i < len(a_list):
        sig = 1
        for letter in a_list[i]:
            sig *= table[letter]
        a_list[i] = [sig, a_list[i]]
        i += 1
    return a_list


# this function find the largest num and return its length
# time complexity O(M+N), space complexity O(M+N)
def find_max(a_list):
    max = 0
    for item in a_list:
        if item[0] > max:
            max = item[0]
    return len(str(max))


# this function equals the digits for all signatures for radix sort
# time complexity O(MN), space complexity O(MN)
def equal_digits(a_list, digits):
    for i in range(len(a_list)):
        a_list[i][0] = "0" * (digits - len(str(a_list[i][0]))) + str(a_list[i][0])
    return a_list


# radix sort the list according to their signatures
# time complexity O(MN), space complexity O(MN)
def radix_sort(a_list, digits):
    # loop for digits times
    for i in range(digits - 1, -1, -1):
        # create count list
        count = []
        for k in range(10):
            temp = []
            count.append(temp)
        # manipulate count according to the list
        for item in a_list:
            count[int(item[0][i])].append(item)
        # create output list and reassign the original list
        output = []
        for group in count:
            for element in group:
                output.append(element)
        a_list = output
    return a_list


# this function change signatures back into integer
# time complexity O(MN), space complexity O(MN)
def back_int(a_list):
    for i in range(len(a_list)):
        a_list[i][0] = int(a_list[i][0])
    return a_list


# this function find the largest group of anagrams
# time complexity O(MN), space complexity O(MN)
def find_max_group(a_list):
    max_index = 0
    max_num = 1
    current_num = 0
    current_index = 0
    old = a_list[0][0]
    # go through the list to check group of anagrams
    for i in range(len(a_list)):
        # check if still in same group, yes num plus one
        if a_list[i][0] == old:
            current_num += 1
        else:
            # in a new group, reset
            current_num = 1
            current_index = i
        # always check if current group is the largest group
        if current_num > max_num:
            max_num = current_num
            max_index = current_index
        old = a_list[i][0]
    return a_list[max_index:max_index+max_num]


# this function ignores the signature of words and only return words
# time complexity O(N), space complexity O(N)
def simplify(a_list):
    output = []
    for item in a_list:
        output.append(item[1])
    return output


# this function get the largest anagram group in a given file
# time complexity O(MN), space complexity O(MN)
def largestAnagrams(file_name):
    the_list = file_oper(file_name)
    the_list = give_sig_all(the_list)
    digits = find_max(the_list)
    the_list = equal_digits(the_list, digits)
    the_list = radix_sort(the_list, digits)
    the_list = back_int(the_list)
    largest_group = find_max_group(the_list)
    output = simplify(largest_group)
    return " ".join(output), the_list


# this function give signature for a string
# time complexity O(k), space complexity O(1)
def give_sig(string):
    sig = 1
    table = {"a": 2, "b": 3, "c": 5, "d": 7, "e": 11, "f": 13, "g": 17, "h": 19, "i": 23, "j": 29, "k": 31, "l": 37,
             "m": 41, "n": 43, "o": 47, "p": 53, "q": 59, "r": 61, "s": 67, "t": 71, "u": 73, "v": 79, "w": 83, "x": 89,
             "y": 91, "z": 101}
    # calculate the signature
    for letter in string:
        sig *= table[letter]
    return sig


# this function search if a sig is in the list and return the index
# time complexity O(logN), space complexity O(1)
def binary_search(a_list, sig):
    start = 0
    end = len(a_list) - 1
    while start <= end:
        mid = (start + end) // 2
        # if in return index
        if a_list[mid][0] == sig:
            return mid
        # if smaller change end
        elif sig < a_list[mid][0]:
            end = mid - 1
        # if bigger change start
        else:
            start = mid + 1
    # if not in return -1
    return -1


# this function get the start index of the anagram group
# time complexity O(W), space complexity O(1)
def find_start_index(a_list, index):
    old = a_list[index][0]
    # keep index decreasing as long as in the same anagram group
    while index >= 0 and a_list[index][0] == old:
        index -= 1
    return index+1


# this function get the anagram group
# time complexity O(W), space complexity O(W)
def get_group(a_list, index):
    sig = a_list[index][0]
    output = []
    # keep appending into output list as long as in same anagram group
    while index < len(a_list) and a_list[index][0] == sig:
        output.append(a_list[index][1])
        index += 1
    return output


# this function check if a string have anagram in the file
# time complexity O(klogN + W), space complexity O(W)
def getScrabbleWord(a_list, string):
    # calculate the sig for the string
    sig = give_sig(string)
    # search if sig is in the list
    index = binary_search(a_list, sig)
    if index == -1:
        return "Not Found!"
    else:
        # get the group start index
        index = find_start_index(a_list, index)
    # get the anagram group
    output = get_group(a_list, index)
    return " ".join(output)


# this function repeat functoin getScrabbleWord for 26 times to generate all possible anagrams
# time complexity O(klogN + W), space complexity O(W)
def getWildCardWords(a_list, string):
    output = []
    # repeat 26 times to check any possible anagrams
    for i in range(ord("a"), ord("z") + 1):
        temp = string
        temp += chr(i)
        # repeat function in task2
        temp_list = getScrabbleWord(a_list, temp)
        if temp_list != "Not Found!":
            output.append(temp_list)
    return " ".join(output)


# main function
if __name__ == "__main__":
    # get largest anagram group
    output, the_list = largestAnagrams("Dictionary.txt")
    print("The largest anagram group is: " + output)
    while True:
        query = input("Enter the query string: ")
        if query == "exit":
            break
        # print anagrams with and without wildcard
        print("The anagram without wildcard are: " + getScrabbleWord(the_list, query))
        print("The anagram with wildcard are: "+ getWildCardWords(the_list, query))