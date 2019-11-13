# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    valued = dict()
    total_value = 0
    for i in range (0, len(prices)):
        valued[i] = (prices[i]/weights[i])
    values = sorted(valued.values())
    # print(values)
    current_capacity = 0
    while (current_capacity < capacity) & (len(values) > 0):
        for key, value in valued.items():
            if value == values[-1]:
                # print(weights[int(key)],prices[int(key)])
                weight = min(weights[int(key)], capacity - current_capacity)
                # print("total capacity left = "+ str(capacity - current_capacity))
                # print ("adding "+str(weight)+" to the capacity")
                current_capacity += weight
                total_value += weight * values[-1]
                # print("total value is : " + str(total_value) + "with capaticy left :" + str(capacity - current_capacity))
        # print("about to reduce the values length from " + str(len(values)) +" to " )
        values.pop()
        # print(str(len(values)))
        # print("current_capacity="+str(current_capacity), "and capacity ="+ str(capacity))
    return total_value




if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))

