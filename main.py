from edapi import EdAPI
from user import init_env
from menu import course_selector, print_menu, print_logo
from leaderboard import print_leaderboard
from ed import update_ed_thread, create_ed_thread, delete_ed_thread

ed = EdAPI()

def main() -> None:
    print_logo()
    ed.login()  # Login with Ed API
    init_env(ed)  # Initialize .env file
    
    while True:
        choice: int = print_menu()

        if choice == '1':
            # Prints leaderboard to terminal
            course_id: int = course_selector(ed)
            print_leaderboard(ed, course_id)

        elif choice == '2':
            # Update leaderboard on Ed Discussions
            course_id: int = course_selector(ed)
            update_ed_thread(ed, course_id)

        elif choice == '3':
            # Create leaderboard on Ed Discussions
            course_id: int = course_selector(ed)
            create_ed_thread(ed, course_id)
            
        elif choice == '4':
            # Delete leaderboard on Ed Discussions
            course_id: int = course_selector(ed)
            delete_ed_thread(ed, course_id)
        
        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid number")


if __name__ == "__main__":
    main()
