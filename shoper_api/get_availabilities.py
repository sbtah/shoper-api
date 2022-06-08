import time
import requests
from shoper_api.token import get_token
from shoper_api.token import SHOPER_STORE


TOKEN = get_token()


# GET https://shop.url/webapi/rest/availabilities
def get_all_availabilities():
    """Return a paginated response with all availabilities in Shoper store."""

    url = f"https://{SHOPER_STORE}/webapi/rest/availabilities"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    res = response.json()
    time.sleep(0.5)

    return res
