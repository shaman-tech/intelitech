from flask import Flask, render_template, request
import logging
import json
from zoomus import ZoomClient, components
from datetime import datetime
from constants import LOG_FILENAME, INTELITECH_API_KEY, INTELITECH_API_SECRET, INTELITECH_HOST_ID

app = Flask(__name__)

logging.basicConfig(filename=LOG_FILENAME, filemode='w', 
                    level=logging.INFO,
                    datefmt='%d-%b-%y %H:%M:%S',
                    format='%(asctime)s - %(levelname)s - %(message)s')


@app.route('/')
def landing_page():
    """Return landing page."""
    return render_template('landing_page.html')

tsj = {
  "name":"Peter Gordon",
  "age": "30",
  "email": "gordon.peter33@gmail.com",
  "appt_date": "06-3-20",
  "appt_time": "10:30 AM"
}

client = ZoomClient(INTELITECH_API_KEY, INTELITECH_API_SECRET)

@app.route('/create_meeting', methods=['POST'])
def create_meeting():
    req_data = request.get_json()
    date_array = req_data["appt_date"].split('-')
    time_array = req_data["appt_time"].split(':')
    mins = time_array[1].split[" "]
    time_array[1] = mins[0]
    if mins[1] == 'PM':
        time_array[0] += 12
    date_time = datetime(2020, date_array[0],date_array[1],time_array[0],time_array[1],0)
    client.meeting.create(
        user_id=INTELITECH_HOST_ID,
        meeting_type=2,
        start_time= date_time,
        duration=20,
        timezone='America/Chicago',
        password='pawpeq',
        topic=f'Consultation with {req_data["name"]}, age {req_data["age"]}',
        agenda=''
    )

    user_list_response = client.user.list()
    user_list = json.loads(user_list_response.content)

    ret_data = {}
    for user in user_list['users']:
        user_id = user['id']
        meeting = json.loads(client.meeting.list(user_id=user_id).content)
        
        topic = meeting["meetings"][0]['topic'])
        if topic.find(req_data["name"]) != -1:
            ret_data["join_url"] = meeting["meetings"][0]['join_url']
            ret_data["start_time"]=meeting["meetings"][0]['start_time']

    return ret_data

    
if __name__ == '__main__':
    app.run(debug=True)