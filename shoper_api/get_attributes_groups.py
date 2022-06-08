import time
import requests
from shoper_api.token import get_token
from shoper_api.token import SHOPER_STORE


TOKEN = get_token()


# GET https://shop.url/webapi/rest/attribute-groups
def get_all_attributes_groups():
    """Return a paginated response with all attributes groups in Shoper store."""

    url = f"https://{SHOPER_STORE}/webapi/rest/attribute-groups"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    res = response.json()
    time.sleep(0.5)

    return res
