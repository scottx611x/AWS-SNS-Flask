# AWS-SNS-Displayer
Handle incoming messages from AWS SNS and display them in a simple webpage

##Installation:

- `$ git clone https://github.com/scottx611x/AWS-SNS-Displayer.git` 
- `$ cd AWS-SNS-Displayer`
- `$ pip install -r requirements.txt`
- `$ python recieve_SNS.py`

## AWS Steps:
- Create a `topic` in the SNS Dashboard
- Create a `subscription` with the `arn` of the topic you just created, and the endpoint being the IP and PORT of the server you are running `recieve_SNS.py` on
- Some port forwarding may be needed at this step on your local network to expose the `PORT` you have set
- Test! In the `topics` section of the SNS dashboard you have an option to publish to a topic. Try this out by publishing some JSON!

TODO:
- [ ] Make a more verbose README
- [ ] Add some styles to the template
