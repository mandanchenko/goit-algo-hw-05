def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    upper_bound = arr[-1]
    counter = 0

    if upper_bound < x:
        return (counter, upper_bound)

    while low <= high:
        counter = counter + 1
        mid = (high + low) // 2

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            upper_bound = arr[mid]
            high = mid - 1

        # інакше x присутній на позиції і повертаємо його
        else:
            return (counter, x)

    # якщо елемент не знайдений
    return (counter, upper_bound)


if __name__ == "__main__":
    arr = [2, 5, 10, 20, 40, 80, 160, 320, 640]
    x = int(input("Enter number: "))
    print(binary_search(arr, x))
