"""Global Company Search — Python example.

pip install apify-client
"""
from apify_client import ApifyClient

APIFY_TOKEN = "YOUR_APIFY_TOKEN"  # https://console.apify.com/account#/integrations

client = ApifyClient(APIFY_TOKEN)

run = client.actor("lentic_clockss/global-company-search").call(
    run_input={
        "searchTerms": ["Tesla Inc", "Samsung Electronics", "DE814764798"],
    }
)

print(f"Run finished. Dataset: {run['defaultDatasetId']}")
print()

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(
        f"{item.get('name', '?'):40s} | "
        f"{item.get('country', '?'):4s} | "
        f"{item.get('status', '?'):12s} | "
        f"{item.get('_source_name', '?')}"
    )
