def offer_rule_1(price):
    # taking lists of discounted items,payable items and a sorted price list in descending order
    sorted_price_list = sorted(price)[::-1]
    discounted_list = []
    payable_list = []

    # sorting the lists according to offer condition
    for i in range(len(sorted_price_list)):
        if i % 2 == 0:
            payable_list.append(sorted_price_list[i])
        else:
            discounted_list.append(sorted_price_list[i])
    return print("Discounted Items = {}".format(discounted_list), "\n", "Payable Items = {}".format(payable_list))


# Example 1
print("Example 1:")
product_price_list = [10, 20, 30, 40, 50, 60]

offer_rule_1(product_price_list)

# Example 2
print("Example 2:")
product_price_list = [10, 20, 30, 40, 50, 50, 60]

offer_rule_1(product_price_list)
