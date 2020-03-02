# Task 51: Coins

def change_coins(amount, coins = [50,20,10,5,2,1]):
    coin_counts = {}

    for coin in coins:
        if not amount: break
        count,amount=divmod(amount,coin)
        if count:
            coin_counts[coin]=count

    return coin_counts