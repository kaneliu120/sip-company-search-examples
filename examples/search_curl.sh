#!/bin/bash
# Global Company Search — cURL example

APIFY_TOKEN="YOUR_APIFY_TOKEN"

# Start the Actor
echo "Starting search..."
RUN=$(curl -s -X POST \
  "https://api.apify.com/v2/acts/lentic_clockss~global-company-search/runs?token=$APIFY_TOKEN&waitForFinish=120" \
  -H "Content-Type: application/json" \
  -d '{"searchTerms": ["Tesla Inc"]}')

DATASET_ID=$(echo "$RUN" | python3 -c "import sys,json; print(json.load(sys.stdin)['data']['defaultDatasetId'])")
echo "Dataset: $DATASET_ID"

# Get results as JSON
echo ""
echo "Results:"
curl -s "https://api.apify.com/v2/datasets/$DATASET_ID/items?token=$APIFY_TOKEN&format=json" | python3 -m json.tool

# Or download as CSV
# curl -s "https://api.apify.com/v2/datasets/$DATASET_ID/items?token=$APIFY_TOKEN&format=csv" > results.csv
