__author__ = 'benfishman'

import requests
from urllib.parse import urljoin
from django.conf import settings


class MailGunWrapper():
    """A wrapper class for the MailGun API"""
    base_url = settings.MAILGUN_BASE_URL
    domain = settings.MAILGUN_DOMAIN
    auth_key = settings.MAILGUN_AUTH_KEY
    from_address = settings.MAILGUN_FROM_ADDRESS

    def send_simple_message(self, to_address, subject, message):
        print(to_address)
        #print(subject)
        #print(message)
        api_end_point = "/messages"
        url = urljoin(self.base_url, self.domain)
        url = url + api_end_point

        print(url)
        x = requests.post(
            url,
            auth=("api", self.auth_key),
            data={"from": self.from_address,
                  "to": to_address,
                  "subject": subject,
                  "text": message})
        return x

    def create_mailing_list(self, list_name, description=None):
        x = requests.post(
            "https://api.mailgun.net/v3/lists",
            auth=('api', self.auth_key),
            data={'address': list_name + '@' + self.domain,
                  'description': description})
        return x

    def add_list_member(self, list, email, description=None, member_name=None, vars=None):
        api_end_point = "/members"
        list_domain = "lists/" + list + "@" + self.domain
        print(self.base_url)
        url = self.base_url + list_domain
        url = url + api_end_point

        x = requests.post(
            url,
            auth=('api', self.auth_key),
            data={'subscribed': True,
                  'address': email,
                  'name': member_name,
                  'description': description,
                  'vars': '{"age": 26}'})
        return x






