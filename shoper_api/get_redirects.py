import json
import time
import requests
from shoper_api.token import get_token
from shoper_api.token import SHOPER_STORE, SHOPER_LOGIN, SHOPER_PASSWORD


TOKEN = get_token()


def get_single_redirect(redirect_id):
    """Return a response with data from single redirect endpoint."""

    url = f"https://{SHOPER_STORE}/webapi/rest/redirects/{redirect_id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    res = response.json()

    return res


# Get data for all redirects from Shoper API.
def get_number_of_redirects_pages():
    """
    Return a reponse with number of pages for all redirects.
    https://shop.url//webapi/rest/redirects
    """

    url = f"https://{SHOPER_STORE}/webapi/rest/redirects"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    res = response.json()
    pages = res.get("pages")

    return pages


def get_list_of_all_redirects_data():
    """
    Returns a list objects of all current redirects on Shoper store.
    """

    redirects = []

    for x in range(1, get_number_of_redirects_pages() + 1):
        data = {"page": f"{x}"}
        url = f"https://{SHOPER_STORE}/webapi/rest/redirects"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        response = requests.get(url, headers=headers, params=data)
        res = response.json()
        items = res.get("list")
        for i in items:
            print(i)
            time.sleep(0.5)
