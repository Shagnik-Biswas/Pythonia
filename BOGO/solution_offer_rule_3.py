def offer_rule_3(price):
    # taking lists of discounted items,payable items and a list to store the index used in loop
    discounted_items = []
    payable_items = []
    idx_lst = []

    # sorting product price list in descending order
    sorted_list = sorted(price, reverse=True)
    copy_sorted_list = sorted_list.copy()

    # sorting lists according to offer conditions
    for i in range(len(sorted_list)):
        if i not in idx_lst:
            if copy_sorted_list[i] == copy_sorted_list[i + 1]:
                payable_items.append(copy_sorted_list[i])
                payable_items.append(copy_sorted_list[i + 1])
                discounted_items.append(copy_sorted_list[i + 2])
                discounted_items.append(copy_sorted_list[i + 3])
                idx_lst.append(i)
                idx_lst.append(i + 1)
                idx_lst.append(i + 2)
                idx_lst.append(i + 3)
            else:
                payable_items.append(copy_sorted_list[i])
                discounted_items.append(copy_sorted_list[i + 1])
                idx_lst.append(i)
                idx_lst.append(i + 1)

    return print("Discounted Items = {}".format(discounted_items), "\n", "Payable Items = {}".format(payable_items))


# Example 1
print("Example 1:")
product_price_list = [10, 20, 30, 40, 40, 50, 60, 60]

offer_rule_3(product_price_list)

# Example 2
print("Example 2:")
product_price_list = [10, 20, 30, 40, 50, 50, 50, 60]

offer_rule_3(product_price_list)
