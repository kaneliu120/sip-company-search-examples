"""Batch search companies from a CSV file.

Input CSV format (one company name per line):
  Tesla Inc
  Samsung Electronics
  Volkswagen AG

pip install apify-client
"""
import csv
import sys

from apify_client import ApifyClient

APIFY_TOKEN = "YOUR_APIFY_TOKEN"
INPUT_CSV = sys.argv[1] if len(sys.argv) > 1 else "companies.csv"
BATCH_SIZE = 10

client = ApifyClient(APIFY_TOKEN)

with open(INPUT_CSV) as f:
    companies = [row[0].strip() for row in csv.reader(f) if row and row[0].strip()]

print(f"Loaded {len(companies)} companies from {INPUT_CSV}")

all_results = []
for i in range(0, len(companies), BATCH_SIZE):
    batch = companies[i : i + BATCH_SIZE]
    print(f"Searching batch {i // BATCH_SIZE + 1}: {batch}")

    run = client.actor("lentic_clockss/global-company-search").call(
        run_input={"searchTerms": batch}
    )

    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        all_results.append(item)
        print(f"  {item.get('name', '?')} | {item.get('country', '?')} | {item.get('_source_name', '?')}")

print(f"\nTotal results: {len(all_results)}")
