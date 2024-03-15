from utils import leaderboard_to_str, create_parameters
import sys

# Return thread id of leaderboard, if found
def find_leaderboard(ed, course_id):
    offset = 0
    thread_count = 0

    while True:
        threads = ed.list_threads(course_id=course_id, limit=100, offset=offset, sort="new")
        for thread in threads:
            if thread["title"] == "Ederboard":
                return thread["id"]
            thread_count += 1

        if len(threads) < 100:
            break
        offset += len(threads)
        
        return 0 

def create_leaderboard(ed, course_id, return_str):
    endorsed_threads = []
    answered_threads = []
    offset = 0
    thread_count = 0

    # Fetch all threads
    while True:
        threads = ed.list_threads(course_id=course_id, limit=100, offset=offset, sort="new")
        for thread in threads:
            thread_count += 1
            sys.stdout.write(f"\rLoading threads & comments: {thread_count}")
            sys.stdout.flush()
            
            if thread['user'] is not None:
                if thread["is_endorsed"]:
                    endorsed_thread = {
                        "user_id": thread["user_id"],
                        "user_name": thread['user']['name']
                    }
                    endorsed_threads.append(endorsed_thread)

            if thread["reply_count"] > 0:
                answered_threads.append(thread)

        if len(threads) < 100:
            break
        offset += len(threads)
    
    # Fetch endorsed answers/comments from answered/commented threads
    def process_comments(thread):
        endorsed_comments = []

        def check_comments(comments):
            for comment in comments:
                if comment.get("is_endorsed", False) and comment.get("user_id"):
                    endorsed_comment = {
                        "user_id": comment["user_id"]
                    }
                    endorsed_comments.append(endorsed_comment)
                if "comments" in comment:
                    check_comments(comment["comments"])

        check_comments(thread.get("comments", []))
        check_comments(thread.get("answers", []))
        return endorsed_comments

    endorsed_comments = []
    for thread in answered_threads:
        endorsed_comments.extend(process_comments(thread))

    # Add endoresed threads to leaderboard
    user_leaderboard = {}
    for endorsed_thread in endorsed_threads:
        user_id = endorsed_thread["user_id"]
        user_name = endorsed_thread["user_name"]
        user_leaderboard[user_id] = {
            "total_endorsements": user_leaderboard.get(user_id, {"total_endorsements": 0})["total_endorsements"] + 1, 
            "name": user_name
        }

    # Add endorsed comments/answers to leaderboard
    for endorsed_comment in endorsed_comments:
        user_id = endorsed_comment["user_id"]
        user_name = endorsed_comment["user_id"]

        if user_id in user_leaderboard:
            user_leaderboard[user_id]["total_endorsements"] += 1
        else:
            user_leaderboard[user_id] = {
                "total_endorsements": 1,
                "name": "User %s" % user_name
            }

    # Sort leaderboard by most endorsements
    sorted_leaderboard = {k: v for k, v in sorted(user_leaderboard.items(), key=lambda y: y[1]["total_endorsements"], reverse=True)}
    leaderboard_str = leaderboard_to_str(ed, sorted_leaderboard)

    if return_str:
        return leaderboard_str
    else:
        return create_parameters(ed, course_id, leaderboard_str)

def print_leaderboard(ed, course_id):
    print()
    print(create_leaderboard(ed, course_id, return_str=True))
