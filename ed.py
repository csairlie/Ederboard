from leaderboard import find_leaderboard, create_leaderboard

def create_ed_thread(ed_obj, course_id):
    ed = ed_obj

    # Check if leaderborad exists on Ed Discussions
    thread_id = find_leaderboard()
    if ederboard_thread_id != 0:
        print("Leaderboard already exists")
        return

    # Create thread parameters with leadeboard string
    parameters = create_leaderboard(ed, course_id, return_str=False)

    # Post thread with parameters
    try:
        leaderboard_thread = ed.post_thread(course_id, parameters)
    except:
        print("Error creating leaderboard thread\n")
        return

# Deletes leaderboard of specified course
def delete_ed_thread(ed, course_id):
    thread_id = find_leaderboard()
    if thread_id == 0:
        print("Error: Leaderboard not found\n")
        return

    parameters = {
        "type": ThreadType,
        "title": "Delete Leaderboard Thread",
        "category": selected_category,
        "content": "",
        "is_pinned": False,
        "is_private": True, 
        "is_anonymous": False,
        "is_megathread": False,
        "anonymous_comments": True,
    }

    try:
        ed.edit_thread(course_id, parameters)
    except:
        print("Error: Unable to delete leaderboard thread.\n")
        return

    print("Leaderboard has been removed and set to private.\n")
    return

def update_ed_thread(ed_obj, course_id):
    ed = ed_obj
    thread_id = find_leaderboard(ed, course_id)
    
    if thread_id != 0:
        parameters = create_leaderboard(ed, course_id, return_str=False)
        thread_id = find_leaderboard(ed, course_id) 
       
       try:
            ed.edit_thread(thread_id, parameters)
        except:
            print("Error updating leaderboard.\n")
            return
    else:
        print("Error: Leaderboard not found.\n")
        return

