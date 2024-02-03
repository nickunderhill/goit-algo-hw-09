def find_min_coins(sum, coins):
    K = [0] + [float('inf') for _ in range(sum)]
    for i in range(1, sum + 1):
        for coin in coins:
            if i - coin >= 0:
                K[i] = min(K[i], K[i - coin] + 1)

    result = {}
    while sum > 0:
        for coin in coins:
            if sum - coin >= 0 and K[sum] == K[sum - coin] + 1:
                result[coin] = result.get(coin, 0) + 1
                sum -= coin
                break
    return result


def main():
    sum = 113
    coins = [50, 25, 10, 5, 2, 1]
    dynamic_change = find_min_coins(sum, coins)
    print(f'Видчача решти динамічним алгоритмом: {dynamic_change}')


if __name__ == "__main__":
    main()
