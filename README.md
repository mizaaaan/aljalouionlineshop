# Al Jaloui Mart

Single-file online store for **Al Jaloui Mart**, 6-B/B, 1st Colony, Mazar Road,
Mirpur-1, Dhaka-1216. Customers browse products, build an order chit and send it
over WhatsApp, or order cash on delivery. English and Arabic UI (Arabic switches the
page to right-to-left).

Live site: **https://mizaaaan.github.io/aljalouionlineshop/**

Every URL in the repo (canonical, Open Graph, structured data, `robots.txt`,
`sitemap.xml`) points at that github.io address, and there is no `CNAME` file, so the
site is self-contained and works the moment a commit lands on `main`.

No build step, no dependencies — `index.html` is the whole site.

## Files

| Path | Purpose |
| --- | --- |
| `index.html` | The entire store (HTML, CSS, JS, product data, translations) |
| `assets/products/*.svg` | Product artwork, one file per product |
| `og-image.png` | 1200×630 social share image (regenerate with `tools/make_og.py`) |
| `tools/make_og.py` | Script that draws `og-image.png` |
| `robots.txt`, `sitemap.xml` | Search engine files for the live github.io URL |
| `404.html` | Branded not-found page GitHub Pages serves for unknown paths |

## Editing the site

Open `index.html` and search for:

- `const PRODUCTS` — products, prices, categories, `rx` flag and image paths
- `const CATEGORIES` — category filter buttons
- `const CONTACT` — order phone number and WhatsApp number
- `const I18N` — every English and Arabic string (`en` / `ar` objects)
- `AL JALOUI` — logo and brand name (header, footer)

Product photos: drop a new image into `assets/products/` and point that product's
`img` field at it.

## Publishing (GitHub Pages)

GitHub Pages serves this repo from the `main` branch, `/ (root)`, at
<https://mizaaaan.github.io/aljalouionlineshop/>. To publish a change, commit and
push to `main`; Pages rebuilds in about a minute.

The canonical link, Open Graph / Twitter image, `robots.txt` and `sitemap.xml` all
use the github.io URL. There is no `CNAME` file in the repo, so Pages never
redirects the working github.io site to another host.

Any other static host works too: upload `index.html`, `assets/`, `og-image.png`,
`robots.txt` and `sitemap.xml`, and serve `index.html` at `/`.

### Attaching a custom domain later (optional)

1. Repository **Settings → Pages → Custom domain**: enter your domain and save
   (this adds a `CNAME` file holding the domain).
2. At your DNS provider point the apex `A` records at GitHub Pages:

   | Type | Name | Value |
   | --- | --- | --- |
   | A | `@` | `185.199.108.153` |
   | A | `@` | `185.199.109.153` |
   | A | `@` | `185.199.110.153` |
   | A | `@` | `185.199.111.153` |
   | CNAME | `www` | `mizaaaan.github.io` |

3. Once DNS resolves to Pages, enable **Enforce HTTPS**.
4. Change the absolute URLs in `<head>` (canonical, `og:url`, `og:image`, Twitter
   image), the JSON-LD `url`/`image`/`logo`, `robots.txt` and `sitemap.xml` from the
   github.io URL to your domain.

## Regenerating the share image

```bash
python3 tools/make_og.py   # needs Pillow; writes og-image.png
```

## Product images

| Product | Image file |
| --- | --- |
| Napa 500mg | `assets/products/napa-500mg.svg` |
| Seclo 20mg | `assets/products/seclo-20mg.svg` |
| Fexo 120mg | `assets/products/fexo-120mg.svg` |
| ORSaline-N | `assets/products/orsaline-n.svg` |
| Baby Diapers (M) | `assets/products/baby-diapers.svg` |
| Baby Lotion 200ml | `assets/products/baby-lotion.svg` |
| Gripe Water 60ml | `assets/products/gripe-water.svg` |
| Hand Sanitizer 200ml | `assets/products/hand-sanitizer.svg` |
| Surgical Face Mask | `assets/products/surgical-mask.svg` |
| Antiseptic Liquid 100ml | `assets/products/antiseptic-liquid.svg` |
| Digital Thermometer | `assets/products/digital-thermometer.svg` |
| Digital Blood Pressure Monitor | `assets/products/blood-pressure-monitor.svg` |
| Glucometer + 10 Strips | `assets/products/glucometer.svg` |
| Multivitamin Tablets | `assets/products/multivitamin.svg` |
| Protein Supplement 400g | `assets/products/protein-supplement.svg` |
