import requests
import os
from urllib.parse import urlparse
from dotenv import load_dotenv
import sys
import argparse


def shorten_link(token, url):
    bitlink_service = "https://api-ssl.bitly.com/v4/bitlinks"
    payload = {"long_url": url}
    response = requests.post(
        bitlink_service,
        headers={"Authorization": "Bearer {}".format(token)},
        json=payload
    )
    response.raise_for_status()
    bitlink = response.json()["id"]
    return bitlink


def count_clicks(token, bitlink):
    bitlink_service =\
                    "https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary"\
                    .format(bitlink)
    payload = {"unit": "day", "units": "-1"}  
    response = requests.get(
        bitlink_service,
        headers={"Authorization": "Bearer {}".format(token)},
        params=payload
    )
    response.raise_for_status()
    clicks_count = response.json()["total_clicks"]
    return clicks_count


def is_bitlink(token, url):
    bitlink_service = "https://api-ssl.bitly.com/v4/bitlinks/{}".format(url)
    response = requests.get(
        bitlink_service,
        headers={"Authorization": "Bearer {}".format(token)}
    )
    return response.ok


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('url')
    return parser


def main():
    load_dotenv()
    token = os.environ['BITLY_TOKEN']
    parser = create_parser()
    namespace = parser.parse_args()
    url = namespace.url
    parsed_url = urlparse(url)
    
    if is_bitlink(token, "{}{}".format(parsed_url.netloc, parsed_url.path)):
        try:
            total_clicks = count_clicks(
                token, "{}{}".format(parsed_url.netloc, parsed_url.path)
            )
            print('Количество кликов', total_clicks)
        except requests.exceptions.HTTPError:
            print("Ошибка запроса")
    else:
        try:
            bitlink = shorten_link(token, url)
            print('Битлинк', bitlink)
        except requests.exceptions.HTTPError:
             print("Ошибка запроса")
            

if __name__ == '__main__':
    main()
