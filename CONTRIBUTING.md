# Contributing to Climate Radar

This is a private project. Contributions are limited to authorized team members.
> Please contact Naif Alsalem for contribution and/or collberation. 

---

## Adding New Signals

1. Identify a new climate development with strategic relevance to Saudi / Arab Group positions
2. Copy the template from `data/signal_template.json`
3. In `index.html`, add the new signal object to `ALL_ALERTS[]`
4. Verify the source link resolves to the correct page
5. Run `python3 scripts/validate_links.py` to confirm the link is live
6. Update `CHANGELOG.md` with the change

**Signal quality checklist:**
- [ ] Link points to the specific page (not homepage)
- [ ] `linkNote` identifies the exact section
- [ ] Summary explicitly mentions Saudi / GCC / Arab Group implications
- [ ] Keywords include relevant technical and institutional terms
- [ ] Risk level is justified in context of Saudi negotiating position
- [ ] Date uses `daysAgo(N)` with appropriate recency

---

## Updating the PIN

1. Decide on a new PIN
2. Generate the hash: `python3 -c "import hashlib; print(hashlib.sha256('NEWPIN'.encode()).hexdigest())"`
3. Replace `CORRECT_HASH` in `index.html`
4. Distribute the new PIN via secure channel to team members
5. Do NOT commit the PIN in plaintext anywhere

---

## Code Style

- All JavaScript uses concise inline style (matching existing code pattern)
- React state kept flat (no nested state objects)
- Inline styles only (no separate CSS files)
- Comments in English

---

## Reporting Issues

Contact Dr. Naif Alsalem directly for any access issues, broken links, or feature requests.
