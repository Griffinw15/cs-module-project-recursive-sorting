# Returns the max profit that can be made with a single buy and sell 
# You have to buy before selling 

# bitcoin_prices = [1050, 270, 1540, 3800, 2]
# find_max_profit(bitcoin_prices)   // should return 3530, 
# which is the max profit you can make from these prices by buying at 270 and selling at 3800

# Why 3800 and 270?
# If we want to the max profit, take the largest price and the smallest price and subtract largest from smallest 
# "You must buy before you sell; no shorting is allowed."
# What does this translate into?
# Whatever price we buy at, we can only subtract that from prices that appear to the left
# of the buying price in order to get our profit.

# 1. Run through multiple examples, including ones you come up with yourself.
# 2. Ask questions as a way to inform a checklist of tasks that need to be handled 

# bitcoin_prices = [10, 7, 5, 8, 11, 9]
# max profit we can make here is buying at 5 and selling at 11 -> 6

# bitcoin_prices = [100, 90, 80, 50, 20, 10]
# since the price keeps dropping all day, we can't make a profit -> 0

# Boils down to: finding the max difference between two prices where the 
# first price is what we buy at and the second price is what we sell at
# taking into account that second price needs to come after the first 
# price in the array 

def find_max_profit(prices):
    # find the largest differences in the values and toss out any 
    # differences that result from shorting (selling before buying)

    # if the first index is the largest value in the entire array, 
    # then our profit is 0 

    # check for the lowest price that's not the last in the array, 
    # buy at this price and check for the max price and sell at that 
    # price. Set a buy and sell variable and compare

    # keep track of current_max
    # loop through all the prices 
        # for each price, subtract every price that comes 
        # before this price from the current price 
        # and see if that results in a larger current_max 