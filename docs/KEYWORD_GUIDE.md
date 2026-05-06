# Keyword Watch System — Guide

## Overview

The Keyword Watch system scans all signal titles, summaries, and internal keyword tags for terms you define. It is designed to surface hidden connections across signals that might not be apparent from titles alone.

---

## Recommended Keyword Sets

### High-Priority Threat Terms
```
phase-out
unabated fossil fuels
CBAM
carbon border
carbon tax
binding target
net zero mandate
fossil fuel subsidy
```

### Negotiation Track Terms
```
Article 6
GST
loss and damage
just transition
NDC
CBDR
historical responsibility
equity
```

### Saudi / Arab Strategic Terms
```
GCC
Arab Group
OPEC
Vision 2030
oil demand
petrochemicals
energy security
natural gas
```

### Institutional Monitoring
```
IPCC
UNFCCC
IEA
UNEP
G7
G20
COP31
COP30
World Bank
```

### Emerging Risk Terms
```
methane
flaring
OGMP
satellite monitoring
carbon market
voluntary carbon
REDD+
blue carbon
```

---

## How the Matching Works

A signal is matched if **any** keyword appears in:
1. The signal **title**
2. The signal **summary**
3. The signal's internal **keyword tags**

Matching is case-insensitive. Partial matches are supported (e.g., "carbon" matches "carbon border", "carbon tax", "carbon market").

---

## Tips

- **Combine broad + specific:** Add both "methane" and "OGMP 2.0" to catch all levels of coverage
- **Use institution names:** Adding "IEA" will surface any signal from or referencing the International Energy Agency
- **Policy codes:** "Article 6", "6.4", "CBAM" are highly specific and low-noise
- **Avoid single letters:** Very short terms produce too many false matches

---

## Exporting Keyword Results

After running a keyword scan, switch to the **KEYWORD RESULTS** tab, then click **⬇ PDF** — the export will reflect only the keyword-matched signals currently visible.
