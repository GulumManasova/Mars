def main():
    cargo_weight = 713
    distance_to_city = 7
    boxes = [0, 0, 0]  # Initialize the array to represent the buried boxes at different distances

    print("Welcome, Martian! You need to mark the locations of the buried cargo.")

    while True:
        print("\nEnter the kilometer mark where you think the cargo is buried:")
        for i in range(3):
            try:
                kilometer_mark = int(input(f"Box {i + 1}: "))
            except ValueError:
                print("Invalid input. Please enter a valid kilometer mark.")
                continue

            # Move the boxes with tentacles
            for j in range(3):
                if j != i:
                    move_box_with_tentacles(boxes, j)

            # Update the location of the current box
            boxes[i] = kilometer_mark

        # Check if the total weight of the found boxes is equal to the cargo weight
        if sum(boxes) == cargo_weight:
            print("\nCongratulations! You've found the cargo.")
            break
        else:
            print("\nOops! The total weight of the boxes is incorrect. Try again.")

    print("\nThank you for your help, Earthling!")

def move_box_with_tentacles(boxes, box_index):
    # Simulate moving the box to a new location
    boxes[box_index] += 1

if __name__ == "__main__":
    main()

