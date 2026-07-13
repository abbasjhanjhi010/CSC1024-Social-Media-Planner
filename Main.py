def main_menu():
    while True:
        print("==============================")
        print("Social Media Content Planner")
        print("==============================")

        print("\n1. Add New Post")
        print("2. Update Post Status")
        print("3. Record Engagement")
        print("4. Display Content Calendar")
        print("5. Generate Performance Report")
        print("6. Export Report")
        print("7. Exit")

        initial_choice = int(input("\nEnter your choice: "))

        match initial_choice:
            case 1:
                new_post_menu()
            case 2:
                post_status_menu()
            case 3:
                engagement_menu()
            case 4:
                content_calendar_menu()
            case 5:
                generate_report_menu()
            case 6:
                export_report_menu()
            case 7:
                print("Exiting main menu...")
                break
            case _:
                print("Enter valid choice (1-7)")


def new_post_menu():
    while True:
        print("==============================")
        print("Add New Post")
        print("==============================")

        print("\n1. (draft)")
        print("2. (schedule: )")
        print("3. Create new")
        print("4. Go to Main menu")
        print("5. Exit")

        first_choice = int(input("\nEnter your choice: "))

        match first_choice:
            case 1:
                print("=")
            case 2:
                print("=")
            case 3:
                print("=")
            case 4:
                break
            case 5:
                print("Exiting new post menu...")
                exit()
            case _:
                print("Enter valid choice (1-5)")


def post_status_menu():
    print("**edit")


def engagement_menu():
    print("**edit")


def content_calendar_menu():
    print("**edit")


def generate_report_menu():
    print("**edit")


def export_report_menu():
    print("**edit")


if __name__ == "__main__":
    main_menu()