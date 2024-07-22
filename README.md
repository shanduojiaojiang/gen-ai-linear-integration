# gen-ai-linear-integration

This is a Gen AI application that integrates with Linear for task management. You can read more about the project requirement/description [here](https://decagon.notion.site/Linear-Integration-Mini-Project-5113994e5c17467bbcb5dc326ae49e40).


The source code is organized under `/src`:
- `main.py`: the main entry for the Linear AI Assistant. 
- `linear_api.py`: this file contains all necessary API calls to Linear.
- `openai_api.py`: this file contains all necessary API calls to OpenAI.
- `config.py`: this file contains config information such as API Keys.

Each function can be unit-tested. To run the whole application, simply change the config file and the transcript in `main.py` and run `python main.py`.