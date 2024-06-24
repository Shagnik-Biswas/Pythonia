def offer_rule_2(price):
    # taking lists of discounted items,payable items
    discounted_items = []
    payable_items = []

    # sorting product price list in descending order
    sorted_list = sorted(price, reverse=True)
    copy_sorted_list = sorted_list.copy()

    # sorting and storing list according to offer condition
    for i in range(len(sorted_list) - 4):
        if i % 2 != 0 and i > 0:
            copy_sorted_list[i], copy_sorted_list[i + 1] = copy_sorted_list[i + 1], copy_sorted_list[i]

    for i in range(len(copy_sorted_list)):
        if i % 2 == 0:
            payable_items.append(copy_sorted_list[i])
        else:
            discounted_items.append(copy_sorted_list[i])

    return print("Discounted Items = {}".format(discounted_items), "\n", "Payable Items = {}".format(payable_items))


# Example 1
print("Example 1:")
product_price_list = [10, 20, 30, 40, 40, 50, 60, 60]

offer_rule_2(product_price_list)

# Example 2
print("Example 2:")
product_price_list = [10, 20, 30, 40, 50, 50, 50, 60]

offer_rule_2(product_price_list)
