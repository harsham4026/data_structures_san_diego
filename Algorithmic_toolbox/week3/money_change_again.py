# python3


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(m):
    coins = (1, 3, 4)

    # initialize minimum number of coins list with max value of m
    min_num_coins = [m] * (m+1)

    # zero money - zero coins
    min_num_coins[0] = 0

    # iterate through all values of money up to m
    for m_i in range(1, m+1):
        # iterate through coins
        for coin in coins:
            # check if coin doesn't exceed money
            if coin <= m_i:
                num_coins = min_num_coins[m_i - coin] + 1

                if num_coins < min_num_coins[m_i]:
                    min_num_coins[m_i] = num_coins

    return min_num_coins[m]


if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
