
def bubble_sort(nlist):
    length = len(nlist)
    
    for x in range(length-1):
        for y in range(0, length - x - 1):
            
            if nlist[y].lower() > nlist[y+1].lower():
                
                tempName = nlist[y]
                nlist[y] = nlist[y+1]
                nlist[y+1] = tempName
                
    return nlist


def insertion_sort(score_list):
   
    for i in range(1, len(score_list)):
        checking = score_list[i]
        j = i - 1

       
        while j >= 0 and score_list[j] > checking:
            score_list[j+1] = score_list[j]
            j = j - 1

        score_list[j+1] = checking
    return score_list


def quick_sort(priceList, calls=[0]):
    
    calls[0] = calls[0] + 1

   
    if len(priceList) <= 1:
        return priceList

    
    mid = len(priceList)//2
    pivot = priceList[mid]

    left = []
    same = []
    right = []

   
    for p in priceList:
        if p < pivot:
            left.append(p)
        elif p == pivot:
            same.append(p)
        else:
            right.append(p)

    
    return quick_sort(left, calls) + same + quick_sort(right, calls)


def main():
    while True:
        print("\n=== Sorting Algorithms Menu ===")
        print("1. Bubble Sort (Names)")
        print("2. Insertion Sort (Scores)")
        print("3. Quick Sort (Book Prices)")
        print("4. Exit program")

        option = input("Enter your choice (1-4): ")

        if option == '1':
            namesList = ["Kado","Bobchu","Zamu","Nado","Lemo",
                        "Sonam","Choki","Tashi","Kinley","Ugyen",
                        "Karma","Phurba","Dechen","Ngawang","Tshering"]

            print("Original list:", namesList)
            
            sortedList = bubble_sort(namesList.copy())
            print("Sorted names:", sortedList)

        elif option == '2':
            testscores = [12,19,22,81,97,96,44,56,59,79,77,27,14]

            print("Original:", testscores)
            print("Sorting... (insertion sort)")
            result = insertion_sort(testscores.copy())
            print("Sorted:", result)

            
            print("Top 5 Scores:")
            top = result[-5:][::-1]
            for rank, value in enumerate(top, 1):
                print(rank, ".", value)

        elif option == '3':
            pricesHere = [450,230,678,125,890,500,655,765]

            print("Original prices:", pricesHere)
            track = [0]    
            finalList = quick_sort(pricesHere.copy(), track)
            print("Sorted prices:", finalList)
            print("Total recursive calls:", track[0])

        elif option == '4':
            print("Alright, exiting now. Thanks for using my program :)")
            break

        else:
            print("Invalid input... pick between 1-4 please")

        again = input("Try another sorting? (y/n): ").lower()
        if again != 'y':
            print("Okay exiting now. Bye!")
            break


if __name__ == "__main__":
    main()