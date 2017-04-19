#!/usr/bin/env python
import zulip
import sys
import env

# Keyword arguments 'email' and 'api_key' are not required if you are
# using ~/.zuliprc
client = zulip.Client(email=env.ZULIP_EMAIL,
                      api_key=env.ZULIP_API_KEY,
                      site=env.ZULIP_SITE)
# Send a stream message
# Static message testing as of now


def send_message():
    client.send_message({
        "type": "stream",
        "to": "bot-testing",
        "subject": "coala loves python",
        "content": "Message is sent successfully!."
    })
# Print each message the user receives
# This is a blocking call that will run forever
client.call_on_each_message(lambda msg: sys.stdout.write(str(msg) + "\n"))

# Print every event relevant to the user
# This is a blocking call that will run forever
# This will never be reached unless you comment out the previous line
client.call_on_each_event(lambda msg: sys.stdout.write(str(msg) + "\n"))
