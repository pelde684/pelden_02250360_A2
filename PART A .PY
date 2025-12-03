def linear_search(student_ids, target):
    comparisons = 0
    for i in range(len(student_ids)):
        comparisons += 1
        if student_ids[i] == target:
            return i + 1, comparisons
    return -1, comparisons


def binary_search(scores, target):

    left = 0
    right = len(scores) - 1
    comparisons = 0

    while left <= right:
        comparisons += 1
        mid = (left + right) // 2

        if scores[mid] == target:
            return mid + 1, comparisons
        elif scores[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, comparisons


def main():

    student_ids = [1001, 1005, 1002, 1008, 1003, 1010, 1004, 1009, 1007, 1012,
                   1011, 1015, 1016, 1006, 1013, 1014, 1018, 1019, 1020, 1021]

    sorted_scores = [45, 52, 58, 63, 67, 72, 75, 78, 82, 85,
                     88, 90, 92, 95, 98, 99, 100, 102, 104, 106]

    while True:
        print("\n=== Searching Algorithms Menu ===")
        print("1. Linear Search - Find Student ID")
        print("2. Binary Search - Find Score")
        print("3. Exit program")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            print(f"Student IDs: {student_ids}")
            try:
                target = int(input("Enter Student ID to search: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            pos, comps = linear_search(student_ids, target)
            if pos != -1:
                print(f"Result: Student ID {target} found at position {pos}")
            else:
                print(f"Result: Student ID {target} not found")
            print(f"Comparisons made: {comps}")

        elif choice == '2':
            print(f"Sorted scores: {sorted_scores}")
            try:
                target = int(input("Enter score to search: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            pos, comps = binary_search(sorted_scores, target)
            if pos != -1:
                print(f"Result: Score {target} found at position {pos}")
            else:
                print(f"Result: Score {target} not found")
            print(f"Comparisons made: {comps}")

        elif choice == '3':
            print("Thank you for using the search program!")
            break

        else:
            print("Invalid choice! Please select 1-3.")

        again = input("Would you like to perform another search? (y/n): ").lower()
        if again != 'y':
            print("Thank you for using the search program!")
            break


if __name__ == "__main__":
    main()