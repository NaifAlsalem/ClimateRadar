# Assets

This directory holds static assets for the Climate Radar platform.

## Contents

| File | Description |
|---|---|
| *(future) logo.svg* | Platform logo for PDF headers and reports |
| *(future) favicon.ico* | Browser tab icon |
| *(future) og-image.png* | Social preview image (for internal wiki embeds) |

## Notes

- All assets must be embeddable as base64 data URIs in `index.html` to maintain the single-file deployment model
- SVG preferred over PNG for logo assets (scalability, smaller size)
- No external asset CDN dependencies — platform must be fully offline-capable
