

# read the file into python and store into a list
# time complexity: O(N), space complexity: O(N)
def file_operation(file_name):
    file = open(file_name, "r")
    contain = []
    # change details about one product into a list and store it in to a table
    for line in file:
        line = line.replace("\n", "")
        line = line.split(":")
        contain.append(line)
    return contain


# compute the maximum profit by only consider the price limit
# time complexity: O(PN), space complexity: O(P+N)
def with_out(products, price_limit):
    # use a memo list of length price limit +1
    memo = [0]*(price_limit+1)
    # use a decision list as same length
    decision = [-1]*(price_limit+1)
    # go through the memo list
    for i in range(1, price_limit+1):
        max_pro = 0
        item_choose = -1
        # every time, check every product if it can be added
        for item in products:
            if int(item[2]) <= i:
                # if can add, get the profit after add this item
                this_pro = int(item[3]) + memo[i-int(item[2])]
                # if the current profit is larger than the max profit, change the max profit to current profit and
                # change the decision
                if this_pro > max_pro:
                    max_pro = this_pro
                    item_choose = int(item[0])
        memo[i] = max_pro
        decision[i] = item_choose
    # print out the result
    print("********** Strategy for price limit **********")
    print_out_without(memo[-1], decision, products)


# compute the maximum profit with both item limit and price limit
# time complexity: O(NPM) where N is the number of products, space complexity: O(MP)
def with_item(products, item_limit, price_limit):
    # use two list as memo
    upper = [0] * (price_limit+1)
    lower = [0] * (price_limit+1)
    # use a table to store decision
    decision_table = []
    for i in range(item_limit):
        # sub_decision is used to store decision for each item limit
        sub_decision = [-1]*(price_limit+1)
        # for every item limit, do as without item limit
        for j in range(1, price_limit+1):
            max_pro = upper[j]
            item_choose = -1
            # go through products
            for item in products:
                if int(item[2]) <= j:
                    # get current profit after choose one item
                    this_value = int(item[3]) + upper[j-int(item[2])]
                    if this_value >= max_pro:
                        # if current profit is larger than max profit, chane max to current and store item chosen in
                        # decision list
                        max_pro = this_value
                        item_choose = int(item[0])
            lower[j] = max_pro
            sub_decision[j] = item_choose
        # append the whole decision list into decision table
        decision_table.append(sub_decision)
        # change upper to lower
        for k in range(len(upper)):
            upper[k] = lower[k]
    print("********** Strategy for both price limit and item limit **********")
    print_out(lower[-1], decision_table, products)


# print out the solution with only price limit
# time complexity: O(P), space complexity: O(P)
def print_out_without(profit, decision, products):
    total_profit = profit
    total_price = 0
    total_item = 0
    solution = {}
    i = len(decision)-1
    # load item chosen from decision list into solution
    while decision[i] != -1:
        if decision[i] not in solution:
            solution[decision[i]] = 1
        else:
            solution[decision[i]] += 1
        # move item chosen to previous
        i -= int(products[decision[i]][2])
    # print solution
    for j in solution:
        print(solution[j], " X ", products[j][1:])
        total_item += solution[j]
        total_price += int(products[j][2])*solution[j]
    print("Total price: ", total_price)
    print("Total item: ", total_item)
    print("Total profit: ", total_profit)


# print ot hte result according to the decision table
# time complexity: O(M), space complexity: O(M)
def print_out(profit, decision_table, products):
    total_profit = profit
    total_price = 0
    total_item = 0
    decision = decision_table[-1][-1]
    solution = []
    # set j to the position of the last element
    j = len(decision_table[-1])-1
    # go through decision table
    for i in range(len(decision_table)-1, -1, -1):
        if decision == -1:
            break
        # add item chosen into solution
        solution.append(decision)
        # move onto previous item
        j -= int(products[decision][2])
        decision = decision_table[i-1][j]
    dic = {}
    # load ite from solution into dic
    for item in solution:
        if item not in dic:
            dic[item] = 1
        else:
            dic[item] += 1
    # print out result
    for key in dic:
        print(dic[key], " X ", products[key][1:])
        total_item += dic[key]
        total_price += int(products[key][2]) * dic[key]
    print("Total price: ", total_price)
    print("Total item: ", total_item)
    print("Total profit: ", total_profit)


if __name__ == "__main__":
    products = file_operation("products.txt")
    while True:
        price_limit = int(input("Enter the price limit: "))
        item_limit = int(input("Enter the item limit: "))
        # print answer for no item limit
        with_out(products, price_limit)
        # print answer for both limits
        with_item(products, item_limit, price_limit)
