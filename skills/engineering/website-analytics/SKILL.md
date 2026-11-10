---
name: website-analytics
description: Set up, audit, or migrate website analytics with Cloudflare Web Analytics, verify collection and private-page exclusions, and optionally connect search visibility reports or clarify social referral measurement.
---

# Website analytics

Make collection repeatable and observable. Start with the site's existing provider and rendering patterns; use Cloudflare Web Analytics when requested or already present. Keep additional providers, custom events, and search tools within the user's requested scope.

## 1. Establish the measurement boundary

Read project instructions, deployment guidance, and existing analytics notes. Inspect the shared layouts, framework integrations, client navigation, environment configuration, CSP, and response headers that affect tracking. With available authorized account access, identify the correct account, hostname, analytics property, injection mode, plan, and existing rules. Reuse an existing property before creating one.

Write a small route matrix: hostname/environment, representative route, expected collection, and reason. Include public pages, exact private route roots and descendants, admin/login/upload routes, unlisted or token-bearing pages, preview hosts, and relevant subdomains. Resolve unknown privacy intent before enabling those routes; work on confirmed public routes meanwhile. Use synthetic URLs in reports.

Clarify the question the user wants answered:

- Website visits, pages, and inbound referrers: browser analytics.
- Search impressions, clicks, and indexing: Search Console or Bing Webmaster Tools.
- Outbound social/contact clicks or bookings: an event-capable measurement workflow.
- AI crawler requests: edge/bot reports; AI recommendations require separate observation.

Done when the current owner, requested measurements, and allowed collection boundary are known. Adding social links does not itself measure their clicks or grant access to social-account analytics.

## 2. Prepare the smallest setup or correction

For Cloudflare, read [the setup and migration reference](references/cloudflare.md). For requested Google/Bing setup, read [search visibility](references/search-visibility.md). For a different existing provider, consult its current official setup and verification documentation rather than transplanting Cloudflare settings.

Choose one injection owner per page. Preserve working tracking unless there is a demonstrated reason to replace it. Automatic injection reduces application maintenance when the supported response paths and exclusions fit; manual rendering gives application-controlled route and environment gates. Compare both against the route matrix before selecting one.

Prepare the code/configuration changes, focused checks, and rollback. Keep existing authorization, cache policy, CSP protections, and opt-outs intact. Use available purpose-built tools or the project's documented CLI; discover current API schemas and required permissions rather than assuming a particular MCP server exists. Request account sign-in or missing credentials through the host's supported secure flow when needed. Read-only audit access is not authorization to change account settings, publish code, or deploy; follow the user's existing authorization and project release rules.

Done when every affected entry point and exclusion is covered, the proposed mode has supported controls, and the change is reviewable. An account setting already matching the target needs verification rather than another mutation.

## 3. Prove collection and exclusion

Run the project's checks for changed code. Verify the delivered response as well as the local build: an edge injector can change HTML after the application renders it.

1. Fetch full HTML and headers from representative allowed and excluded routes, following redirects. Expect exactly one intended beacon on allowed documents and none on excluded documents. A HEAD response cannot establish script presence.
2. In an authorized browser test, confirm the script loads and actual beacon requests succeed at the expected destination without CSP errors. Trigger navigation and page lifecycle flushing as needed. A synthetic endpoint probe does not prove the website sends valid data.
3. Test direct loads and public → private → public navigation, including back/forward and client transitions. Inspect flushed payloads for excluded paths. A beacon initialized on a public page may survive client navigation; absence from the destination HTML alone is insufficient.
4. Check the correct dashboard property, host, and test time window after its documented delay. Confirm the expected public path appears. Multiple lifecycle requests do not necessarily mean duplicate pageviews.

Use an isolated environment when project policy requires it; keep preview traffic out of production reports unless explicitly chosen for a controlled test. Inspect payloads locally and retain only redacted evidence; raw HAR files and access URLs can expose private data.

Done when each route-matrix case has a result and code checks pass. If account access, deployment authorization, or collection delay prevents proof, leave that stage explicitly unverified rather than claiming end-to-end success.

## 4. Leave an operator handoff

Save a short guide in the project's documentation: provider/property label, injection owner, exclusions and their enforcement point, where to view reports, validation date/results, rollback, and remaining gaps. Reference configuration paths instead of duplicating tokens or identifiers. Public documentation uses placeholders; credentials stay in the project's secret store.

Report these stages separately: configured locally, delivered by the edge, browser transport accepted, dashboard observed. Describe what each report measures. Missed history is not recovered by repairing a beacon; browser blockers and missing referrers leave gaps. Avoid blanket consent or compliance claims based on a provider's marketing description.

The [candidate comparison](https://github.com/Today20092/skills/blob/main/research/website-analytics-skills-2026-11-06.md) explains why this skill exists; consult it only when evaluating alternatives, not for routine setup. It lives in the source repository rather than the installed skill bundle.
