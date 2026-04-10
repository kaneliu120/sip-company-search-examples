# Global Company Search — Examples & Integration Guide

Search company registrations across **40+ countries** and **82 official government registries** in a single query. Real-time data from official sources — no third-party API keys needed.

**Apify Store**: [lentic_clockss/global-company-search](https://apify.com/lentic_clockss/global-company-search)

## What It Does

Enter a company name, registration number, LEI code, or VAT ID — get results from official government registries worldwide. Three-tier smart routing automatically detects the query type and routes to the right registries.

**Supported registries include**: US SEC EDGAR, UK Companies House, EU VIES VAT, GLEIF LEI, German Handelsregister, French RCS, Japan EDINET, Australia ASIC, Canada Corporations, and 70+ more.

## Quick Start

### Python

```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_TOKEN")

run = client.actor("lentic_clockss/global-company-search").call(
    run_input={"searchTerms": ["Tesla Inc", "Samsung Electronics"]}
)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(f"{item['name']} | {item['country']} | {item['status']} | {item['_source_name']}")
```

### JavaScript

```javascript
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: 'YOUR_APIFY_TOKEN' });

const run = await client.actor('lentic_clockss/global-company-search').call({
    searchTerms: ['Tesla Inc', 'Samsung Electronics'],
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
items.forEach(item => {
    console.log(`${item.name} | ${item.country} | ${item.status} | ${item._source_name}`);
});
```

### cURL

```bash
# Start the Actor
curl -X POST "https://api.apify.com/v2/acts/lentic_clockss~global-company-search/runs?token=YOUR_APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"searchTerms": ["Tesla Inc"]}'

# Get results (use the defaultDatasetId from the run response)
curl "https://api.apify.com/v2/datasets/DATASET_ID/items?token=YOUR_APIFY_TOKEN"
```

## Input Options

| Parameter | Type | Description |
|-----------|------|-------------|
| `searchTerms` | string[] | Company names, registration numbers, LEI codes, or VAT IDs |

The Actor automatically detects query type:
- **Company name** → broadcasts to all relevant registries
- **LEI code** (20 chars alphanumeric) → routes to GLEIF
- **VAT ID** (e.g. `DE123456789`) → routes to EU VIES
- **Registration number with country suffix** (e.g. `12345678.GB`) → routes to specific country registry

## Output Fields

Each result contains:

| Field | Description |
|-------|-------------|
| `name` | Company/entity name |
| `type` | Entity type (Corporation, LLC, etc.) |
| `status` | Registration status (Active, Dissolved, etc.) |
| `country` | ISO-2 country code |
| `authority` | Issuing authority name |
| `_source_name` | Human-readable source name |
| `_source_authority` | Official authority |
| `_data_freshness` | real-time, cached, or preloaded |
| `_response_time_ms` | Source response time |
| `_collected_at` | UTC timestamp |
| `raw_fields` | Original fields from the source registry |

## Integration Examples

### Google Sheets (via Apify Integration)

1. Go to [Apify Integrations](https://apify.com/integrations)
2. Connect Google Sheets
3. Set the Actor to run on a schedule
4. Results automatically append to your spreadsheet

### n8n Workflow

1. Add an **Apify** node
2. Select `lentic_clockss/global-company-search`
3. Set input: `{"searchTerms": ["Company Name"]}`
4. Connect output to your CRM, database, or notification service

### Zapier

1. Trigger: Schedule or webhook
2. Action: Run Apify Actor → `lentic_clockss/global-company-search`
3. Action: Send results to Google Sheets / Slack / Email

### Python Batch Processing

```python
from apify_client import ApifyClient
import csv

client = ApifyClient("YOUR_APIFY_TOKEN")

# Read company names from CSV
with open("companies.csv") as f:
    companies = [row[0] for row in csv.reader(f)]

# Search in batches of 10
for i in range(0, len(companies), 10):
    batch = companies[i:i+10]
    run = client.actor("lentic_clockss/global-company-search").call(
        run_input={"searchTerms": batch}
    )
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        print(f"{item.get('name')} | {item.get('country')} | {item.get('_source_name')}")
```

## Sample Output

```json
{
  "name": "TESLA, INC.",
  "type": "Corporation",
  "status": "Active",
  "country": "US",
  "authority": "SEC EDGAR",
  "_source_name": "US SEC EDGAR Company Search",
  "_source_authority": "U.S. Securities and Exchange Commission",
  "_data_freshness": "real-time",
  "_response_time_ms": 342,
  "_collected_at": "2026-04-10T12:00:00Z",
  "raw_fields": {
    "cik": "1318605",
    "entity_name": "TESLA, INC.",
    "state_of_incorporation": "DE",
    "sic": "3711",
    "sic_description": "Motor Vehicles & Passenger Car Bodies"
  }
}
```

## Pricing

- **$0.005** per Actor start
- **$0.003** per company record returned
- Free tier available on Apify

## Related Actors

| Actor | Description |
|-------|-------------|
| [Global Sanctions Screening](https://apify.com/lentic_clockss/global-sanctions-screening) | Screen against OFAC, EU, UN sanctions lists |
| [Regulatory Compliance Search](https://apify.com/lentic_clockss/regulatory-compliance-search) | Search regulatory filings and compliance data |
| [Google Maps Scraper](https://apify.com/lentic_clockss/google-maps-scraper) | Extract business data, reviews, and contact info from Google Maps |

## License

MIT
