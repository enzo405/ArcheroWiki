import requests
import json

MATOMO_TOKEN = "*************"
MATOMO_INSTANCE = "******************"


def extract_subdirectories(page_data, current_url=""):
    # Recursive function to extract subdirectories and their URLs
    subdirectories = {}

    for subpage in page_data:
        sublabel = subpage.get("label", "")
        suburl = subpage.get("url", "")
        sublabel: str = f"{current_url}/{sublabel}" if current_url else sublabel

        # Check if there's a nested subtable
        if "subtable" in subpage:
            # Recursive call for nested subtables
            subdirectories.update(extract_subdirectories(subpage["subtable"], sublabel))
        elif suburl is not None and "?_x_tr_sl" not in suburl:
            subdirectories[sublabel] = suburl

    return subdirectories


def get_top_pages():
    """
    Makes an API Call to the Matomo API to retrieve the most searched titles page.
    Return a dictionary containing the first 10 pages.
    Each item of the dictionary is made of the label and the url of the page.
    """
    params = {
        "module": "API",
        "method": "Actions.getPageUrls",
        "idSite": 1,
        "period": "month",
        "date": "today",
        "format": "json",
        "filter_limit": 1,
        "token_auth": MATOMO_TOKEN,
        "expanded": 1,
    }

    response = requests.get(f"{MATOMO_INSTANCE}/index.php", params=params)
    response.raise_for_status()
    data = response.json()

    wiki_label_data = data[0].get("subtable", [{"label": "wiki"}])[0]

    if wiki_label_data:
        en_subdirectories = extract_subdirectories(wiki_label_data.get("subtable", []))
        return en_subdirectories

    return None


# Example usage
if __name__ == "__main__":
    result = get_top_pages()

    if result is not None:
        print("Subdirectories for 'en' label:")
        with open("web-project\calculator\data\label_url.json", "w") as outfile:
            json.dump(result, outfile)
    else:
        print("Failed to retrieve subdirectories.")
