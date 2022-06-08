from shoper_api.get_collections import (
    get_all_collections,
    get_single_collection,
    get_all_products_for_collection,
)
from shoper_api.get_options import get_all_options, get_single_option
from shoper_api.get_attributes import get_all_attributes
from shoper_api.get_attributes_groups import get_all_attributes_groups
from shoper_api.get_products import get_single_product
from shoper_api.get_metafields import get_all_metafields
from shoper_api.get_options_groups import get_all_options_groups


def main():
    print(get_all_options_groups())


if __name__ == "__main__":
    main()
