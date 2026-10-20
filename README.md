# khanson.io

Kyle Hanson's personal site. Static HTML, CSS, and a little JavaScript, with locally hosted fonts and no runtime dependencies.

## Local preview

Run `npm run dev`, then visit <http://127.0.0.1:4321>. Requires Python 3. No package installation or build is needed. Run `npm run check` to check assets, anchors, structured data, and publishing files.

Content lives in `site/index.html`, styling in `site/assets/styles.css`, and the optional copy-email interaction in `site/assets/site.js`. The site remains usable without JavaScript.

## GitHub Pages

`.github/workflows/deploy.yml` validates and publishes only `site/` on every push to `main`. It can also be run manually. Set **Settings → Pages → Source** to **GitHub Actions** and set the custom domain to **khanson.io**. A custom domain must be set in Pages settings (or via the API); the `CNAME` file alone does not configure it for Actions deployments.

## Domain setup

The domain currently uses Namecheap BasicDNS and URL forwarding. In Namecheap's **Advanced DNS** for `khanson.io`, replace the apex (`@`) URL Redirect record with these four records:

| Type | Host | Value |
| --- | --- | --- |
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | hansonkd.github.io |

Use Automatic TTL. Preserve mail-related MX/TXT records. Once GitHub's DNS check passes and the certificate is ready, enable **Enforce HTTPS** in Pages settings. DNS changes and certificate provisioning can take up to 24 hours.

Reference: [GitHub's custom domain documentation](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).

## Assets & content

- Career dates and roles, consumer product work, trust company formation, and regulatory work supplied by Kyle Hanson; current CTO title confirmed by the [GetDynasty team page](https://www.getdynasty.com/team/).
- Portrait: [Kyle's GetDynasty team photo](https://www.getdynasty.com/images/team/kyle-hanson.jpg), stored locally.
- DM Sans and Instrument Serif are distributed under the SIL Open Font License. License files are included in `site/assets/fonts/`.

This repository publishes only the public website; do not add credentials or private material to `site/`.
