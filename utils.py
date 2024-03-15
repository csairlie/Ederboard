from edapi import EdAPI
import pprint

def leaderboard_to_str(ed_obj, user_leaderboard):
    ed = ed_obj
    # Returns string for printing/update Ed Thread
    content = "\n--- Ederboard ---\n"
    for user_id, data in user_leaderboard.items():
        name = data['name']
        total_endorsements = data['total_endorsements']
        content += f"{name}: {total_endorsements}\n"
    return content

def create_parameters(ed_obj, course_id, leaderboard_str):
    ed = ed_obj
    # Prompt for what category to post the leaderboard in
    thread_categories = []
    user = ed.get_user_info()
    courses = user["courses"]
    for course in courses:
        if course['course']['id'] == course_id:
            for category in course['course']['settings']['discussion']['categories']:
                thread_categories.append(category['name']) 
    index = 0
    print("Select Category to post leaderboard thread:\n")
    for category in thread_categories:
        print(f"{index}: {category}")
        index += 1

    while True:
        try:
            choice = int(input())
            if 1 <= choice <= len(thread_categories):
                selected_category = thread_categories[choice - 1]
                break
            else:
                print("Invalid choice. Please select your desired category.")
        except ValueError:
                print("Invalid input. Please select your desired category.")

    # Prompt whether to pin learboard or not
    choice = input("Would you like to pin the leaderboard thread?\n Yes(1) or No (2): ")
    if choice == 1:
        pinned = True
    elif choice == 2:
        pinned = False
    else:
        print("Invalid choice. Please enter a valid number")

    # Set parameters of thread
    parameters = {
        "type": ThreadType,
        "title": "Ederboard", 
        "category": selected_category,
        "content": formatted_entries,
        "is_pinned": pinned,
        "is_private": False,
        "is_anonymous": False,
        "is_megathread": False,
        "anonymous_comments": True,
    }
    return parameters

