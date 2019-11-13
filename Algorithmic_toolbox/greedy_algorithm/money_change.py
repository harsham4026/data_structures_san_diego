# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3

    change = money % 10
    if change == 5:
        return int(money/10) +1
    elif change >= 5:
        return int(money/10) + (change-4)
    else:
         return int(money/10) + change




if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))

