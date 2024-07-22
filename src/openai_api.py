import json
import openai

def classify_conversation(transcript, api_key):
    """ This function uses GPT-4o to classify the given conversation transcript.
    """
    openai.api_key = api_key
    prompt = """
    You are a helpful assistant that classifies conversation transcripts. In the given transcript,
    there could be a feature request, a bug report, or neither/none. Assume that there is at most one of each.
    """
    try:
        response = openai.ChatCompletion.create(
            model = "gpt-4o",
            messages = [
                {"role": "system", "content": prompt},
                {"role": "user", "content": transcript}
            ],
            functions = [
                {
                    "name": "classify_conversation",
                    "description": "Classifies a conversation transcript has a feature request, bug report, or neither.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "classification": {
                                "type": "string",
                                "enum": ["feature_request", "bug_report", "none"]
                            }
                        },
                        "required": ["classification"]
                    }
                }
            ],
            function_call={"name": "classify_conversation"}
        )
        # Parse the string back into dictionary
        result = json.loads(response["choices"][0]["message"]["function_call"]["arguments"])["classification"]
        print(f"classify_conversation(): Successfully classified transcription as {result}")
        return result
    
    except Exception as e:
        print(f"classify_conversation(): Error classifying transcript. Exception: {str(e)}")
        return None


def find_similar_task(transcript, existing_tasks, api_key):
    """
    This function uses GPT-4o to find a similar task in the existing tasks list.
    """
    openai.api_key = api_key
    prompt = """
    You are a helpful assistant that checks if the given transcript is related to one of the
    existing tasks.
    """
    try:
        for task in existing_tasks:
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": f"Transcript: {transcript}\nTask: {task['title']} {task['description']}"}
                ],
                functions=[
                    {
                        "name": "find_similar_task",
                        "description": "Checks if the task is similar to the transcript.",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "similar": {
                                    "type": "boolean"
                                }
                            },
                            "required": ["similar"]
                        }
                    }
                ],
                function_call={"name": "find_similar_task"}
            )
            similar = json.loads(response["choices"][0]["message"]["function_call"]["arguments"])["similar"]
            if similar:
                print(f"find_similar_task(): Found similar task with ID {task['id']}")
                return task["id"]

        print("find_similar_task(): No similar task found")
        return None
    
    except Exception as e:
        print(f"find_similar_task(): Error finding similar task. Exception: {str(e)}")
        return None

# print("SJ testing!!!")
# tasks = [
#     {'id': '6c408c81-4ac4-4dd6-910a-dc55b195d547', 
#      'title': 'SJ test 2', 
#      'description': 'creating test2'}, 
#      {'id': '5ad3172f-85d6-4b36-8ad5-940601b1c5a9', 
#       'title': 'SJ test 1', 
#       'description': 'creating test 1'}
#       ]
# find_similar_task("SJ testing 2", tasks, 'sk-None-TaWRC5UMEM1bRpptrONlT3BlbkFJk5ZmszCuHwMqoH5jX5DU')
# classify_conversation("testing tesing", 'sk-None-TaWRC5UMEM1bRpptrONlT3BlbkFJk5ZmszCuHwMqoH5jX5DU')
