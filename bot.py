#!/usr/bin/env python
import zulip
import sys
import env
import requests


class cobotZulip():

    def __init__(self, zulip_api, zulip_email, zulip_site):
        self.email = zulip_email
        self.site = zulip_site
        self.api = zulip_api
        self.client = zulip.Client(
            email=self.email, api_key=self.api, site=self.site)

    def respond(self, msg):
        content = msg['content'].strip().encode('utf-8')
        print content

    def send_message(self, content, type, to, subject):
        response = self.client.send_message({
            "type": type,
            "to"	: to,
            "subject"	: subject,
            "content"	: content
        })
        print response

    def main(self):
        self.send_message("Hello", "stream", "bot-testing", "Subject")
        self.client.call_on_each_event(
            lambda msg: sys.stdout.write(str(msg) + "\n"))
        self.client.call_on_each_message(self.respond)

if __name__ == "__main__":
    zulip_api = env.ZULIP_API_KEY
    zulip_email = env.ZULIP_EMAIL
    zulip_site = env.ZULIP_SITE
    bot = cobotZulip(zulip_api, zulip_email, zulip_site)
    bot.main()
