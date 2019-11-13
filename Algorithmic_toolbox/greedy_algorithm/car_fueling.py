# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    current_distance = 0
    current_refill_index = 0
    current_refill_point = 0
    stops.append(d)
    num_refill = 0
    while current_distance + m < d:
        if stops[current_refill_index +1] -stops[current_refill_index] > m:
            return -1
        for refill in range(current_refill_index, len(stops)):
            if stops[refill] - current_refill_point > m:
                current_refill_index = refill - 1
                current_refill_point = stops[current_refill_index]
                current_distance = stops[refill - 1]
                num_refill += 1
                # print ("car refilled at : " + str(stops[refill - 1]) + ", with num of refills :" + str(num_refill))
                break
            else:
                current_distance = stops[refill]
                # print("car reached at :" + str(stops[refill]))

    return num_refill



if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))

