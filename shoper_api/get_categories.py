import time
import httpx
import asyncio
from shoper_api.token import SHOPER_STORE, SHOPER_LOGIN, SHOPER_PASSWORD, TOKEN


# GET https://shop.url/webapi/rest/categories
async def get_all_categories():
    """Return a paginated response with all products and number of pages."""

    async with httpx.AsyncClient() as client:
        url = f"https://{SHOPER_STORE}/webapi/rest/categories"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        response = await client.get(url, headers=headers)

        yield response.json()


async def show_off():
    async with httpx.AsyncClient() as client:
        headers = {"Authorization": f"Bearer {TOKEN}"}
        url = f"https://{SHOPER_STORE}/webapi/rest/categories"
        response = await client.get(url, headers=headers)
        print(response.json().get("pages"))
