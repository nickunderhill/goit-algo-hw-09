def find_coins_greedy(sum, coins):
    result = {}
    for coin in coins:
        if sum >= coin:
            count = sum // coin
            result[coin] = count
            sum -= coin * count
    return result


def main():
    sum = 113
    coins = [50, 25, 10, 5, 2, 1]
    gready_change = find_coins_greedy(sum, coins)
    print(f'Видчача решти жадібним алгоритмом:   {gready_change}')


if __name__ == "__main__":
    main()
