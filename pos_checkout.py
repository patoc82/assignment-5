
def get_student_seed():
    student_key = input("Student key: ")
    return sum(ord(ch) for ch in student_key.strip())


def get_item_name():
    while True:
        item_name = input("Item name (or DONE): ").strip()

        if item_name.upper() == "DONE":
            return "DONE"

        if item_name:
            return item_name

        print("Item name cannot be blank. Try again.")


def get_unit_price():
    while True:
        try:
            unit_price = float(input("Unit price: "))

            if unit_price > 0:
                return unit_price

            print("Unit price must be greater than 0.")
        except ValueError:
            print("Invalid price. Enter a number.")


def get_quantity():
    while True:
        try:
            quantity = int(input("Quantity: "))

            if quantity >= 1:
                return quantity

            print("Quantity must be at least 1.")
        except ValueError:
            print("Invalid quantity. Enter a whole number.")


def main():
    seed = get_student_seed()

    subtotal = 0.0
    total_units = 0

    while True:
        item_name = get_item_name()

        if item_name == "DONE":
            break

        unit_price = get_unit_price()
        quantity = get_quantity()

        subtotal += unit_price * quantity
        total_units += quantity

    if total_units >= 10 or subtotal >= 100:
        discount_percent = 10
    else:
        discount_percent = 0

    discount_amount = subtotal * (discount_percent / 100)
    total = subtotal - discount_amount

    if seed % 2 == 1:
        total = max(0.0, total - 3.00)
        perk_applied = "YES"
    else:
        perk_applied = "NO"

    print(f"Seed: {seed}")
    print(f"Units: {total_units}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: {discount_percent}%")
    print(f"Perk applied: {perk_applied}")
    print(f"Total: ${total:.2f}")


if __name__ == "__main__":
    main()