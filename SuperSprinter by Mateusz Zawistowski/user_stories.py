in_memory_user_stories = [
    {
        "Id": 1,
        "Story Title": "First User Story",
        "User Story": "This is my first user story in this web application",
        "Acceptance Criteria": "It just works",
        "Business Value": 1000,
        "Estimation": 2,
        "Status": "In Progress"
    },
    {
        "Id": 2,
        "Story Title": "Second User Story",
        "User Story": "This is my second user story in this web application",
        "Acceptance Criteria": "It just works too!",
        "Business Value": 500,
        "Estimation": 8,
        "Status": "TODO"
    },
    {
        "Id": 3,
        "Story Title": "Third User Story",
        "User Story": "This is my third user story in this web application",
        "Acceptance Criteria": "Works, I guess...?",
        "Business Value": 2000,
        "Estimation": 1,
        "Status": "Done"
    },
]

in_memory_dictionary_keys = [
    "Id", "Story Title", "User Story", "Acceptance Criteria", "Business Value", "Estimation", "Status"
]


def greatest_id():
    return max([user["Id"] for user in in_memory_user_stories])


def add_user_story(user_story):
    in_memory_user_stories.append(user_story)


def get_user_story(user_story_id):
    for user_story in in_memory_user_stories:
        if user_story["Id"] == user_story_id:
            return user_story
    return None


def update_user_story(user_story):
    for story in in_memory_user_stories:
        if story["Id"] == user_story["Id"]:
            story["Story Title"] = user_story["Story Title"]
            story["User Story"] = user_story["User Story"]
            story["Acceptance Criteria"] = user_story["Acceptance Criteria"]
            story["Business Value"] = user_story["Business Value"]
            story["Estimation"] = user_story["Estimation"]
            story["Status"] = user_story["Status"]
