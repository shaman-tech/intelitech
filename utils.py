import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "newagent-xdceeg-a9ce3d2fd472.json"

import dialogflow_v2 as dialogflow
_session_client = dialogflow.SessionsClient()
PROJECT_ID = "newagent-xdceeg"

def detect_intent(text, session_id, language_code='en'):
    session = _session_client.session_path(PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = _session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result

def fetch_reply(query, session_id):
    response = detect_intent(query,session_id)
    return response.fulfillment_text