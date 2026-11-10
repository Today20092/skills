# Optional search visibility setup

Use this branch when the user requests search reporting or indexing checks. Search ownership and browser analytics are independent; neither guarantees indexing or AI recommendations.

## Establish ownership

Inspect existing properties with authorized access before creating another. Use the correct owner account and host scope. Google Search Console Domain properties use DNS verification; URL-prefix properties have other verification methods. Preserve existing verification records. When a new DNS record is required and authorized, add the exact provided value without replacing unrelated TXT records, then verify ownership through the provider. Keep account sessions and credentials out of notes.

If sign-in is needed, hand off through the host's supported sign-in flow and resume after access is available. Record inaccessible reports as pending rather than inferring that a property does not exist.

Sources: [Google property types](https://support.google.com/webmasters/answer/34592?hl=en), [ownership verification](https://support.google.com/webmasters/answer/9008080?hl=en).

## Submit and inspect

Discover the actual production sitemap URL from the project's generated output and `robots.txt`; avoid guessing `sitemap.xml` versus `sitemap-index.xml`. Check its full GET response, valid XML, and canonical public URLs before submitting it. Check for an existing submission first.

Record submission acceptance separately from fetched/processed status and discovered pages. An initial fetch failure can change after processing; inspect the reported error and HTTP behavior before editing site code. Use a bounded recheck and leave a follow-up if processing is still pending.

Inspect a representative service page in Search Console. Distinguish indexed status from a live test showing the page is eligible to be indexed. Request indexing only within the authorized workflow; queue acceptance is not indexing completion. Public `site:` searches do not establish authoritative indexing status.

Sources: [sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview), [URL inspection](https://support.google.com/webmasters/answer/9012289?hl=en).

## Bing and handoff

With permission, import the relevant verified properties from Google Search Console into Bing, or follow Bing's independent verification flow. Inspect the imported property and sitemap state rather than assuming import completed everything. Authentication can differ between providers even in the same browser.

Leave links to the property's Performance and indexing reports with their current processing status. Explain that social-account analytics, website referral traffic, and outbound clicks are separate measurements. A social-profile property is not a substitute for native platform analytics, and an external profile does not need the website's XML sitemap.

Source: [Bing add/verify/import](https://www2.bing.com/webmasters/help/add-and-verify-site-12184f8b).
