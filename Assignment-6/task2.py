def print_first_ten_multiples(number: int) -> None:
    for i in range(1, 11):
        print(number * i)


def classify_age(age: int) -> str:
    if age < 0:
        return "Invalid age"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teen"
    elif age <= 64:
        return "Adult"
    else:
        return "Senior"


if __name__ == "__main__":
    n = int(input("Enter a number: ").strip())
    print_first_ten_multiples(n)

    age = int(input("Enter age to classify: ").strip())
    print(classify_age(age))


