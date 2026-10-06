# Travels (wonbo.site/travel/)

A travel blog built with Jekyll. It is a GitHub Pages project site, so it inherits the custom domain of the home page (wonbo.site) and is served at `wonbo.site/travel/`.

## One-time setup

1. Set the repo's **Settings → Pages → Build and deployment → Source** to **GitHub Actions**.
   (A plugin generates the per-country and per-year pages, so the site is built by `.github/workflows/pages.yml` instead of the default build.)
2. Add a link to `/travel/` from the home page repo.

## URLs

| URL | What it is |
| --- | --- |
| `/travel/` | All trips, newest first, with tabs for Korea · Japan · Singapore · Other |
| `/travel/2025-tokyo/` | A single trip |
| `/travel/2025-tokyo/day-2/` | A sub-page of that trip (optional) |
| `/travel/country/japan/` | Trips by country (generated) |
| `/travel/year/2025/` | Trips by year (generated) |

## Writing a new trip

1. **Shrink the photos.** Put the originals in `raw/2026-osaka/` and run the script. `raw/` is never committed.
   ```sh
   pip install pillow            # once (plus pillow-heif for iPhone HEIC)
   python3 scripts/resize_photos.py raw/2026-osaka 2026-osaka --rename
   ```
   This saves 1600px WebP files as `assets/photos/2026-osaka/01.webp, 02.webp …` and strips GPS and other location data.

2. **Create the post.** `_trips/2026-osaka.md`
   ```yaml
   ---
   title: Osaka, 3 days
   date: 2026-05-01          # departure date, used for the year pages and sorting
   end_date: 2026-05-03      # optional
   countries: [japan]        # several countries: [japan, korea]
   cover: 01.webp            # cover photo shown in the lists
   summary: One-line summary
   album_url: https://...    # optional: link to the full album (Google Photos etc.)
   ---
   ```
   Add photos in the body like this:
   ```liquid
   {% include photo.html src="03.webp" caption="Dotonbori" %}
   ```

3. **To split it by day**, create files in a folder with the same name, such as `_trips/2026-osaka/day-2.md`. They are listed under the trip automatically.

4. **New countries**: add a `slug: Display name` line to `_data/countries.yml`. Change which countries get their own home-page tab with `featured_countries` in `_config.yml`.

## Planning upcoming trips

Write a trip you haven't taken yet the same way in `_trips/`, and add `planned: true`.

- It appears under **Upcoming trips** at the top of the home page, in date order, with a "Plan" badge before the title.
- It stays out of the country and year lists and the region tabs.
- After the trip, delete `planned: true` and add a `cover`, photos and the write-up. The URL stays the same.

Plan posts can list structured data in the front matter and render it with a single line in the body. Copy the format from the example post.

| Line in the body | Front matter | Renders |
| --- | --- | --- |
| `{% include flights.html %}` | `flights:` | Flight cards |
| `{% include itinerary.html %}` | `days:` | Day-by-day timeline |
| `{% include restaurants.html city="chengdu" %}` | `restaurants: { chengdu: [...] }` | Restaurant cards with dietary warnings (`tallow` beef-tallow broth, `beef`, `cheese`, `shellfish`, `ok` nothing to avoid) |

Example: `_trips/2026-chengdu-chongqing.md`

## Preview locally

```sh
bundle install
bundle exec jekyll serve
# http://localhost:4000/travel/
```

## Storage

Each photo is roughly 200–400KB, so the repo's recommended 1GB is enough for dozens of trips. Don't commit originals; upload them to an album service and link it with `album_url`. If space runs low later, move only the photos to external storage (Cloudflare R2 etc.) and change the paths.
