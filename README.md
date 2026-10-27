# khanson.io

Kyle Hanson's personal site. Static HTML, CSS, and a little JavaScript, with locally hosted fonts and no runtime dependencies.

## Local preview

Run `npm run dev`, then visit <http://127.0.0.1:4321>. Requires Python 3. No package installation or build is needed. Run `npm run check` to check assets, anchors, structured data, and publishing files.

Content lives in `site/index.html`, styling in `site/assets/styles.css`, and the optional copy-email interaction in `site/assets/site.js`. The site remains usable without JavaScript.

Follow the [editorial style guide](docs/editorial-style.md) when editing copy.

## GitHub Pages

`.github/workflows/deploy.yml` validates and publishes only `site/` on every push to `main`. It can also be run manually. Set **Settings → Pages → Source** to **GitHub Actions** and set the custom domain to **khanson.io**. A custom domain must be set in Pages settings (or via the API); the `CNAME` file alone does not configure it for Actions deployments.

## Domain setup

The domain is registered at Namecheap. Cloudflare's free plan is configured to manage DNS, while GitHub Pages hosts the site. Namecheap's **Custom DNS** setting contains these assigned nameservers:

- `adele.ns.cloudflare.com`
- `melnicoff.ns.cloudflare.com`

Cloudflare contains the following website records:

| Type | Host | Value |
| --- | --- | --- |
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | hansonkd.github.io |

All five website records use Automatic TTL and **DNS only**. The five existing Google mail MX records and the Google verification TXT record were imported and verified against Namecheap's records.

The nameserver change was saved on October 21, 2026. Cloudflare is waiting for the registrar change to propagate. Once GitHub's DNS check passes and its certificate is ready, enable **Enforce HTTPS** in Pages settings. Do not enable Cloudflare's proxy while certificate provisioning is pending. DNS changes and certificate provisioning can take up to 24 hours.

References: [GitHub custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site), [Cloudflare nameserver setup](https://developers.cloudflare.com/dns/zone-setups/full-setup/setup/).

## Assets & content

- Career dates and roles supplied by Kyle Hanson; current CTO title confirmed by the [GetDynasty team page](https://www.getdynasty.com/team/).
- Technical and operating contributions supplied by Kyle on October 27, 2026: Carta data-model refactors to support products, reconciliation to catch cap-table drift and potential errors, ACH payment reconciliation with a direct bank connection, and management of technical-debt risk; Docker sandboxes for automated grading of client assessments at Hired; and consumer product development, trust administration software, design and implementation of a custom CRM to centralize client communications, trust company formation, compliance, and regulatory work at GetDynasty.
- Portrait: [Kyle's GetDynasty team photo](https://www.getdynasty.com/images/team/kyle-hanson.jpg), stored locally.
- DM Sans and Instrument Serif are distributed under the SIL Open Font License. License files are included in `site/assets/fonts/`.

### Public technical sources

Reviewed Kyle’s [public GitHub profile](https://github.com/hansonkd) and repository documentation on October 27, 2026. The following sources support the open-source project descriptions. Company-specific contributions come from Kyle’s account; the repositories do not establish which technologies those companies used.

| Project | Source | Details used on the site |
| --- | --- | --- |
| Puff | [README](https://github.com/hansonkd/puff/blob/master/readme.md), [Cargo manifest](https://github.com/hansonkd/puff/blob/master/Cargo.toml) | Python and Rust runtime with PostgreSQL, Redis, GraphQL, and background tasks. The manifest names Kyle as the author. |
| Tino | [README](https://github.com/hansonkd/Tino/blob/master/README.md) | Python remote function calls over the Redis wire protocol with MessagePack. This uses the protocol, not necessarily a Redis server. |
| BundleDB | [README](https://github.com/hansonkd/bundledb/blob/master/readme.md) | Experimental embedded database in Go. The README identifies it as pre-alpha and not used in production. |
| Skyline | [README](https://github.com/hansonkd/skyline/blob/master/README.md) | MQTT message broker in Elixir. The README describes an early implementation with missing protocol features. |

This repository publishes only the public website; do not add credentials or private material to `site/`.
