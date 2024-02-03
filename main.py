import timeit
import dynamic_change_alg as dynamic
import gready_change_alg as gready


RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
COLOR_END = '\033[0m'


def compare_algorithms(sum, coins):
    result = dict()

    result["Gready"] = timeit.timeit(
        lambda: gready.find_coins_greedy(sum, coins), number=10)
    result["Dynamic"] = timeit.timeit(
        lambda: dynamic.find_min_coins(sum, coins), number=10)

    return result


def print_results(results):
    header = f"| {'Algorithm':<20} | {'Execution time':<15} |"
    separator = "| " + "-"*20 + " | " + "-"*15 + " |"
    row_template = "| {key:<20} | {value:^15.5f} |"
    footer = "| " + "-"*38 + " |"

    print(header)
    print(separator)
    for key, value in results.items():
        print(row_template.format(key=key, value=value))
    print(footer)


def main():

    coins = [50, 25, 10, 5, 2, 1]
    sum = 1000000


    print(YELLOW + "\nStarting alogirhtms time execution comparison..." + COLOR_END)

    results = compare_algorithms(sum, coins)
    print_results(results)


if __name__ == "__main__":
    main()
