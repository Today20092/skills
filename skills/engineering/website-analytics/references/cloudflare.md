# Cloudflare Web Analytics

Documentation checked 2026-11-06. Recheck current official documentation and actual account entitlements before changing settings. This is an original workflow; linked documentation owns the product facts.

## Select the injection owner

| Mode                         | Use when                                                                 | Verify before enabling                                                                                                     |
| ---------------------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| Zone automatic injection     | Traffic is proxied and edge controls can preserve the route matrix.      | Relevant hostnames/subdomains, existing manual scripts, exclusions, CSP, and actual delivered HTML.                        |
| Manual snippet               | The application needs explicit route/host gates or traffic is DNS-only.  | Property is in manual mode, the official snippet uses the beacon token, and all intended rendering boundaries are covered. |
| Cloudflare Pages integration | The deployed product is Pages and its integration fits the route policy. | Its next-deployment lifecycle and overlap with zone injection or a manual embed.                                           |

Use the snippet/token provided by the existing Web Analytics property. The site's management identifier (`site_tag`) is not the beacon token (`site_token`). Match fields by meaning through the current schema or dashboard, never by their similar shape. Keep real identifiers out of reusable examples. A public beacon token is browser configuration, not an API credential.

For a migration, record the old mode and application gates. Prepare exclusions and verify they can operate before enabling broad injection. Coordinate disabling the previous owner and enabling the new one; validate after each change, and restore the old mode if exclusions or collection fail. Check all layouts and integrations for duplicate injection. Restoring manual mode also requires restoring its script if removed.

Sources: [setup](https://developers.cloudflare.com/web-analytics/get-started/), [FAQ](https://developers.cloudflare.com/web-analytics/faq/), [Pages integration](https://developers.cloudflare.com/pages/how-to/web-analytics/), [site API](https://developers.cloudflare.com/api/resources/rum/subresources/site_info/).

## Preserve exclusions

Inspect current rule capacity and deployment behavior; the following controls are distinct:

- **Web Analytics rules** operate on proxied sites. The documented Free-plan quota is zero; other plans have different quotas. Check [limits](https://developers.cloudflare.com/web-analytics/limits/) and [analytics rules](https://developers.cloudflare.com/web-analytics/configuration-options/rules/).
- **Configuration Rules** provide `disable_rum: true` for matching requests and are available on Free with their own quotas. This setting takes precedence over enabling Web Analytics rules. Match the intended hostname plus exact route roots and descendants; `/admin/` alone misses `/admin`. Preserve existing rule order and settings. These rules do not prove an application-embedded or already-running script has stopped. See [availability](https://developers.cloudflare.com/rules/configuration-rules/) and [Disable RUM](https://developers.cloudflare.com/rules/configuration-rules/settings/#disable-real-user-monitoring-rum).
- **Response `no-transform`** can prevent automatic injection. Cloudflare documents the `public, no-transform` case. Preserve existing private/no-store directives if adding this directive; never make a private response public for analytics. It also affects transformations, so use it only with an understood response policy and delivered-response verification. See [setup caveat](https://developers.cloudflare.com/web-analytics/get-started/) and [cache-control behavior](https://developers.cloudflare.com/cache/concepts/cache-control/).

Choose the smallest control that expresses the project's policy. Verify private and error responses as well as happy-path pages. An exclusion is collection prevention, not a dashboard filter or access-control mechanism. If automatic injection cannot preserve the boundary, keep manual rendering with explicit public-route and environment gates.

## CSP and delivery

Check the effective policy, including `script-src-elem`, nonces, and `strict-dynamic` where present. Permit `https://static.cloudflareinsights.com` in the applicable script policy without broad wildcards or weakening unrelated restrictions.

Automatic injection uses a same-origin collection endpoint; manual installation uses `https://cloudflareinsights.com` according to the setup FAQ. Allow only the destination the chosen mode needs in `connect-src`, and verify actual browser requests. A successful script fetch does not prove collection is permitted. See [CSP guidance](https://developers.cloudflare.com/web-analytics/faq/) and [data collection](https://developers.cloudflare.com/web-analytics/data-metrics/data-origin-and-collection/).

Automatic injection happens downstream of the local build. Fetch the final full HTML GET and headers for both public and excluded documents after deployment; check cache behavior and redirects. Preserve response privacy and authorization while debugging missing injection.

## Client navigation

The beacon can track SPA transitions through browser navigation APIs. Withholding a script on an excluded document does not unload one initialized earlier. Test transitions across the privacy boundary, then trigger deferred metrics and inspect payload paths. A full document navigation across that boundary can provide isolation when proven in the application; disabling SPA handling alone still needs lifecycle tests. Manual embedding supports `spa: false`; use current supported snippet options rather than patching the vendor script. See [SPA behavior](https://developers.cloudflare.com/web-analytics/get-started/web-analytics-spa/).

## Interpret the result

Use real browser-generated requests to test transport, then confirm the path appears in the correct property after the documented processing delay. Keep script delivery, accepted transport, and dashboard visibility as separate results. If a stage remains unavailable, report it and the next check rather than repeatedly changing a working setup.

Cloudflare Web Analytics reports pages and inbound referrers; it currently lacks custom events and UTM reporting. It does not measure outbound Instagram/WhatsApp clicks or completed bookings by merely embedding the beacon. Offer an event-capable provider or a scoped redirect measurement only when those outcomes are requested. Native social-platform reporting requires access to that platform. Sources: [dimensions](https://developers.cloudflare.com/web-analytics/data-metrics/dimensions/), [FAQ](https://developers.cloudflare.com/web-analytics/faq/).

Edge requests and AI-crawler activity count a different population from browser visits. User-agent names alone do not verify crawler identity, and crawler access does not prove a recommendation or citation in an AI answer. Treat unavailable recommendation tests as unknown.
