from dotenv import dotenv_values, set_key
import os

def check_env(ed) -> None:
    # Checks if proper fields exist in .env file.
    # If not, intialize fields and values
    env_values = dotenv_values('.env')

    if 'ED_API_TOKEN' not in env_values:
        api_token = input("Enter your Ed API Token: ")
        set_key('.env', 'ED_API_TOKEN', api_token)

    if 'COURSE_IDS' not in env_values or 'COURSE_CODES' not in env_values:
        course_ids, course_codes = get_courses(ed)
        set_key('.env', 'ED_COURSE_IDS', ','.join(map(str, course_ids)))
        set_key('.env', 'ED_COURSE_CODES', ','.join(course_codes))

def get_courses(ed):
    user = ed.get_user_info()
    courses = user["courses"]
    course_ids = []
    course_codes = []

    for course in courses:
        course_ids.append(course['course']['id'])
        course_codes.append(course['course']['code'])

    return course_ids, course_codes

def init_env(ed) -> None:
    # Checks if .env exists. If so, check if valid. If not, create .
    env_exists = os.path.isfile("./.env")
    if not env_exists:
        with open(".env", "w") as f:
            pass
        check_env(ed)
    else:
        check_env(ed)