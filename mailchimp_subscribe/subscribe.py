import requests

url_template = 'https://{}.api.mailchimp.com/3.0/lists/{}/members'

def subscribe(api_key, list_id, email_address):
    data_center = api_key.split('-')[1]
    url = url_template.format(data_center, list_id)

    data = {
        'email_address': email_address,
        'status': 'subscribed',
    }
    requests.post(url, json=data, auth=('mailchimp_subscribe', api_key))
