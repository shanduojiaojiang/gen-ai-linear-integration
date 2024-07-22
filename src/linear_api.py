import requests
from config import LINEAR_API_URL, HEADERS

def get_team_id():
    """ API function call to Linear to get the Team ID.
    """
    try:
        query = """
        query Teams {
            teams {
                nodes {
                    id
                    name
                }
            }
        }
        """
        response = requests.post(
            LINEAR_API_URL,
            headers=HEADERS,
            json={'query': query}
        )
        if response.status_code == 200 and response.json()["data"]["teams"]["nodes"]:
            team_id = response.json()["data"]["teams"]["nodes"][0]["id"]
            print(f"get_team_id(): Successfully found team ID {team_id}")
            return team_id
        else:
            print(f"get_team_id(): Failed to get team ID. Response: {response.json()}")
            return None
    except Exception as e:
        print(f"get_team_id(): Error finding team ID. Exception: {str(e)}")
        return None


def create_linear_task(teamID, title, description):
    """ API function call to Linear to create an issue/task based on the title and description.
    """
    try:
        query = """
        mutation {
            issueCreate(
                input: {
                    teamId: "%s",
                    title: "%s",
                    description: "%s"
                }
            ) {
                success
                issue {
                    id
                }
            }
        }
        """ % (teamID, title, description)
        response = requests.post(
            LINEAR_API_URL,
            headers=HEADERS,
            json={'query': query}
        )
        if response.status_code == 200 and response.json()["data"]["issueCreate"]["issue"]["id"]:
            task_id = response.json()["data"]["issueCreate"]["issue"]["id"]
            print(f"create_linear_task(): Successfully created Linear task {task_id}")
            return task_id
        else:
            print(f"create_linear_task(): Failed to create Linear task. Response: {response.json()}")
            return None
        
    except Exception as e:
        print(f"create_linear_task(): Error creating Linear task. Exception: {str(e)}")
        return None


def fetch_existing_tasks():
    """ API function call to Linear to fetch all existing tasks
    """
    try:
        query = """
        query {
            issues {
                nodes {
                    id
                    title
                    description
                }
            }
        }
        """
        response = requests.post(
            LINEAR_API_URL,
            headers=HEADERS,
            json={'query': query}
        )
        if response.status_code == 200 and response.json()["data"]["issues"]["nodes"]:
            tasks = response.json()["data"]["issues"]["nodes"]
            print(f"fetch_existing_tasks(): Successfully fetched {len(tasks)} Linear tasks.")
            return tasks
        else:
            print(f"fetch_existing_tasks(): Failed to fetch Linear tasks. Response: {response.json()}")
            return None
    
    except Exception as e:
        print(f"fetch_existing_tasks(): Error fetching Linear task. Exception: {str(e)}")
        return None


def add_comment_to_task(task_id, comment):
    """ API function call to Linear to add a comment to a specific task
    """
    try:
        query = """
        mutation {
            commentCreate(
                input: {
                    issueId: "%s",
                    body: "%s"
                }
            ) {
                success
            }
        }
        """ % (task_id, comment)

        response = requests.post(
            LINEAR_API_URL,
            headers=HEADERS,
            json={'query': query}
        )
        if response.status_code == 200 and response.json()["data"]:
            print(f"add_comment_to_task(): Successfully added comment to task {task_id}")
            return response.json()
        else:
            print(f"add_comment_to_task(): Failed to add comment to task. Response: {response.json()}")
            return None
    
    except Exception as e:
        print(f"add_comment_to_task(): Error adding comment to Linear task. Exception: {str(e)}")
        return None
    
# get_team_id()
# create_linear_task("7ac8c5fb-b65a-4f9b-8be8-2720ec29349e", "SJ test 2", "creating test2")
# print(fetch_existing_tasks())
# add_comment_to_task("6c408c81-4ac4-4dd6-910a-dc55b195d547", "I just want to see if this works ahhaha")
