// Global Company Search — JavaScript example
// npm install apify-client

import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: 'YOUR_APIFY_TOKEN' });

const run = await client.actor('lentic_clockss/global-company-search').call({
    searchTerms: ['Tesla Inc', 'Samsung Electronics', 'DE814764798'],
});

console.log(`Run finished. Dataset: ${run.defaultDatasetId}\n`);

const { items } = await client.dataset(run.defaultDatasetId).listItems();

for (const item of items) {
    console.log(`${item.name} | ${item.country} | ${item.status} | ${item._source_name}`);
}
