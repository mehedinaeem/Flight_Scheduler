# main.py
def main():
    while True:
        print("1. Search Flight")
        print("2. Book a flight")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # See flight details
            import flight
            print("1. Book a Flight:")
            print("2. Exit:")
            choice1 = input("Enter your choice:")
            if choice1 == "1":
                # Book a flight
                import user
            elif choice1 == "2":
                break

        if choice == "2":
            # Get user information and store in the database
            import user

        elif choice == "3":
            break

if __name__ == "__main__":
    main()
