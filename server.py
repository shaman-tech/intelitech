from flask import Flask, render_template, request
import logging
import json
import string
import random
from zoomus import ZoomClient, components
from datetime import datetime
from constants import LOG_FILENAME, INTELITECH_API_KEY, INTELITECH_API_SECRET, INTELITECH_HOST_ID

app = Flask(__name__)

logging.basicConfig(filename=LOG_FILENAME, filemode='w', 
                    level=logging.INFO,
                    datefmt='%d-%b-%y %H:%M:%S',
                    format='%(asctime)s - %(levelname)s - %(message)s')


def password_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

@app.route('/')
def landing_page():
    """Return landing page."""
    return render_template('landing_page.html')

client = ZoomClient(INTELITECH_API_KEY, INTELITECH_API_SECRET)

@app.route('/create_meeting', methods=['POST'])
def create_meeting():
    req_data = request.get_json()['data']
    date_array = req_data["appt_date"].split('-')
    time_array = req_data["appt_time"].split(':')
    mins = time_array[1].split(" ")
    time_array[1] = mins[0]
    if mins[1] == 'PM':
        time_array[0] = int(time_array[0]) + 12
    date_time = datetime(2020, int(date_array[1]), int(date_array[0]), int(time_array[0]),int(time_array[1]),0)
    meeting = client.meeting.create(
        user_id=INTELITECH_HOST_ID,
        meeting_type=2,
        start_time= date_time,
        duration=20,
        timezone='America/Chicago',
        password=password_generator(),
        topic=f'Consultation with {req_data["name"]}, age {req_data["age"]}',
        settings={
            "auto_recording":"True",
            "host_video":True,
            "participant_video":True,
        },
        registrants_email_notification=True,
        agenda=f'{req_data["agenda"]}'
    )

    # user_list_response = client.user.list()
    # user_list = json.loads(user_list_response.content)

    # ret_data = {}
    # for user in user_list['users']:
    #     user_id = user['id']
    #     meeting = json.loads(client.meeting.list(user_id=user_id).content)
    #     ret_data[user_id] = meeting
        # topic = meeting["meetings"][0]['topic']
        # if topic.find(req_data["name"]) != -1:
        #     ret_data["join_url"] = meeting["meetings"][0]['join_url']
        #     ret_data["start_time"]=meeting["meetings"][0]['start_time']
        #     return ret_data
    return meeting.content

    
if __name__ == '__main__':
    app.run(debug=True)