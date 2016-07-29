from flask import Flask, render_template, request, url_for
import json
import time
import sys

messages = []
IP_TO_SERVE_ON = "0.0.0.0"
PORT = 80

# Initialize the Flask application
app = Flask(__name__)

# Route that can handle `GET` and `POST` requests and provide the POST-ed
# SNS messages to the rendered template


@app.route('/', methods=['GET', 'POST'])
def handle_requests():
    global messages

    if request.method == 'POST':
        sys.stdout.write("Message Recieved")
        request_content = json.loads(request.get_data())
        sys.stdout.write(request_content)

        # Insert newest messages to front of list
        messages.insert(0, request_content["Message"])
        return str(len(messages))

    if request.method == 'GET':
        return render_template('SNS.html', message_queue=messages)

# Route that will clear all messages


@app.route('/clear')
def clear():
    global messages

    # Clear all messages and re-render the template
    messages = []
    return render_template('SNS.html', message_queue=messages)

# Run the app :)
if __name__ == '__main__':
    app.run(
        host=IP_TO_SERVE_ON,
        port=PORT,
        threaded=True
    )

