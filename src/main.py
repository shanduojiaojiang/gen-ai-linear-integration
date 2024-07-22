from config import OPENAI_API_KEY
from openai_api import classify_conversation, find_similar_task
from linear_api import get_team_id, create_linear_task, fetch_existing_tasks, add_comment_to_task


def handle_transcript(transcript):
    """ This is the main function that takes in the conversation transcript, classifies whether
        the transcript, and performs corresponding downstream tasks.
    """
    print(">>> Linear AI Assistant: Classifying transcript...")
    task = classify_conversation(transcript, OPENAI_API_KEY)
    if task == "none":
        print(">>> Linear AI Assistant: No action needed")
        return "Linear Integration: No action needed"

    existing_tasks = fetch_existing_tasks()
    similar_task_id = find_similar_task(transcript, existing_tasks, OPENAI_API_KEY)

    if similar_task_id:
        print("\n>>> Linear AI Assistant: Found similar task ID, adding comment...")
        response = add_comment_to_task(similar_task_id, transcript)
    else:
        team_id = get_team_id()
        title = f"{task.replace('_', ' ').capitalize()}"
        print("\n>>> Linear AI Assistant: creating a new", title, "...")
        response = create_linear_task(team_id, title, transcript)
    
    return response


# Example usage
if __name__ == "__main__":
    transcript = "can we add a function to delete all files"
    response = handle_transcript(transcript)