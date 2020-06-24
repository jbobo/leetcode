def max_profit(array):
    """This is an implementation of Kadane's Algorithm."""
    # init with first index
    max_profit = 0
    min_price = array[0]

    # loop over the rest of the array
    for _, current_price in enumerate(array[1:]):
        # check if we've found a new minimum,
        # if we have, move the trailing pointer.
        if current_price < min_price:
            min_price = current_price
        # Check if we've found a new maximum
        # if we have, update the leading pointer.
        elif (current_price - min_price) > max_profit:
            max_profit = current_price - min_price

    return max_profit


if __name__ == "__main__":
    stock_prices = [7, 1, 5, 3, 6, 4]
    print(stock_prices, "\n", max_profit(stock_prices))
