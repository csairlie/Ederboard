from user import get_courses

def course_selector(ed):
    course_ids, course_codes = get_courses(ed)
    print("Which course?\n")
    index = 1
    
    for course_id, course_code in zip(course_ids, course_codes):
        print(f"{index}: {course_code}")
        index += 1
    print(f"{len(course_ids)+1}: Go back")
    
    while True:
            try:
                choice = int(input("\nInput: "))
                if 1 <= choice <= len(course_ids):
                    selected_course_id = course_ids[choice - 1]
                    return selected_course_id

                elif choice == len(course_ids)+1: 
                    return

                else:
                    print("Invalid choice. Please select your desired course.")
            except ValueError:
                print("Invalid input. Please select your desired course.")

def print_menu():
    print("\n----- MENU -----\n")
    print("1. View Leaderboard")
    print("2. Update Leaderboard")
    print("3. Create Leaderboard")
    print("4. Delete Leaderboard")
    print("5. Quit")
    return input("\nSelect (1/2/3/4/5): ")

def print_logo():
    print("""
         ______    __          __                         __
        / ____/___/ /__  _____/ /_  ____  ____ __________/ /
       / __/ / __  / _ \/ ___/ __ \/ __ \/ __ `/ ___/ __  / 
      / /___/ /_/ /  __/ /  / /_/ / /_/ / /_/ / /  / /_/ /  
     /_____/\__,_/\___/_/  /_.___/\____/\__,_/_/   \__,_/   
                                                       
    """)
