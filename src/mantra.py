'''
hit a rest endpoint every hour with some data in a payload
'''
import os
import time
import requests


def main():
    while True:
        time.sleep(60*60*1)
        url = 'https://mantra.com/api/v1/evrmore-node/active'
        payload = {
            #'ip': 'evrmore-node', server will deduce this
            'port': 50002,
            'address': os.environ.get('DONATION_ADDRESS', 'EcMeJ7KPPkCKd4cNfZjCRFE4WCPmY5M9LH'),
        }
        headers = {
            'Content-Type': 'application/json'
        }
        try:
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                print('Success:', response.json())
            else:
                print('Error:', response.status_code, response.text)
        except requests.exceptions.RequestException as e:
            print('Request failed:', e)


if __name__ == '__main__':
    main()
