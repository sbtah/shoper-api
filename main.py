import asyncio
from shoper_api.get_collections import (
    get_all_collections,
    get_single_collection,
    get_all_products_for_collection,
)
from shoper_api.get_options import get_all_options, get_single_option
from shoper_api.get_attributes import get_all_attributes
from shoper_api.get_attributes_groups import get_all_attributes_groups
from shoper_api.get_products import (
    get_single_product,
    get_list_of_all_shoper_product_ids,
)
from shoper_api.get_metafields import get_all_metafields
from shoper_api.get_options_groups import get_all_options_groups
from shoper_api.get_categories import get_all_categories, show_off


def main():
    # asyncio.run(show_off())
    asyncio.run(print(get_all_categories()))


# def main():
#     print(get_single_product(102))


if __name__ == "__main__":
    main()
