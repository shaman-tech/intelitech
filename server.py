from flask import Flask, render_template
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



client = ZoomClient(INTELITECH_API_KEY, INTELITECH_API_SECRET)
date_time = datetime(2020, 6,4,15,25,24)
@app.route('/create_meeting')
def create_meeting():
    client.meeting.create(
    user_id=INTELITECH_HOST_ID,
    meeting_type=2,
    start_time= date_time,
    duration=30,
    timezone='America/Chicago',
    password='pawpeq',
    topic='Healing the wounds'

)
# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)