import sys
from src.equipment import display_equipment
from src.booking import create_booking, get_booking_records


def run_cli():
    while True:
        print("\n========================================")
        print("       LAB EQUIPMENT BOOKING SYSTEM")
        print("========================================")
        print("1. View Equipment")
        print("2. Book Equipment")
        print("3. View Booking Records")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_equipment()

        elif choice == "2":
            display_equipment()
            equipment_id = input("\nEnter equipment ID: ").strip()

            try:
                quantity = int(input("Enter quantity: ").strip())
            except ValueError:
                print("Booking rejected: Quantity must be a whole number.")
                continue

            booking_date = input("Enter booking date (YYYY-MM-DD): ").strip()
            print("\n" + create_booking(equipment_id, quantity, booking_date))

        elif choice == "3":
            records = get_booking_records()
            print("\nBooking Records")
            print("-" * 45)
            if not records:
                print("No booking records found.")
            else:
                for record in records:
                    print(
                        f"#{record['booking_id']} | {record['equipment']} | "
                        f"Qty: {record['quantity']} | {record['date']} | "
                        f"{record['status']}"
                    )

        elif choice == "4":
            print("\nThank you for using the system.")
            break

        else:
            print("\nInvalid choice. Please try again.")


def main():
    if "--cli" in sys.argv:
        run_cli()
    else:
        try:
            from src.app_gui import run_gui
            run_gui()
        except ImportError as error:
            print("Could not start the desktop interface.")
            print("Make sure Python Tkinter is installed.")
            print(f"Details: {error}")
            print("You can still use CLI mode with: python -m src.main --cli")


if __name__ == "__main__":
    main()
