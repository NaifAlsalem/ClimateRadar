# Keyword Watch System

## Overview

The Keyword Watch system scans every signal's title, summary, and topic tags for terms that we already define.
The goal is to surface connections across signals that a quick read of the headlines would miss, and to make sure nothing relevant to our priorities slips through during a high-volume scan.

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
All keywords are managed directly in the Keyword Watch bar at the top of the Intelligence Feed. Type a term in the input field and press Enter to add it. Keywords appear as chips and can be removed at any time by clicking the x next to them. Once your list is set, click SCAN and switch to the KEYWORD RESULTS tab to see what matched.

A few things worth keeping in mind as you build your watchlist:

- **Combine broad + specific:** Adding both "methane" and "OGMP 2.0" at the same time means you will catch general methane coverage as well as signals specifically referencing the Oil and Gas Methane Partnership framework. One does not replace the other.
- **Use institution names:** Typing "IEA" and pressing Enter will surface any signal that mentions the International Energy Agency, whether it is the original source or just referenced in the text.
- **Policy codes:** Terms like "Article 6", "CBAM", and "GST" are specific enough that almost every result they return will be relevant. These are worth keeping in your watchlist permanently during active negotiation cycles.
- **Avoid single letters:** A single word like "gas" or "oil" will match too many unrelated signals and make the results hard to read. Use "natural gas", "oil demand", or "fossil fuel" instead to keep results focused.

---

## Exporting Keyword Results

After running a keyword scan, switch to the **KEYWORD RESULTS** tab, then click **PDF** and the export will reflect only the keyword-matched signals currently visible.
