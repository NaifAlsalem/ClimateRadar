# Signal Taxonomy & Risk Classification

## Signal Categories

| Category | Description | Example Sources |
|---|---|---|
| **Narrative** | Language shifts in major reports that could reframe global climate discourse | IPCC reports, IEA scenarios, UNEP assessments |
| **Policy** | Regulatory developments with direct trade or compliance implications | EU CBAM, carbon market rules, national legislation |
| **Negotiation** | Texts, drafts, or leaks from formal UNFCCC negotiation tracks | GST outcomes, COP agendas, SB session notes |
| **Finance** | Climate finance pledges, fund governance, MDB commitments | G7 communiqués, Loss & Damage fund, GCF decisions |
| **Alliance** | Bloc formations, coalition positions, joint declarations | AU declarations, Arab Group statements, LMDC positions |
| **Strategic** | Assessments relevant to Saudi/Arab strategic positioning | Vision 2030 reviews, OPEC+ context, bilateral analyses |

---

## Risk Level Definitions

### 🔴 HIGH
Signals that pose an **immediate or near-term strategic threat** to Saudi / Arab Group negotiating positions or economic interests. Requires active response, counter-narrative preparation, or diplomatic escalation.

**Criteria:**
- Binding or near-binding language in major international texts
- Policy with direct trade/fiscal impact (e.g., CBAM expansion)
- Narrative shifts that could reduce negotiating space
- Coalition formations that isolate Arab positions

### 🟡 MEDIUM
Signals that represent **developing threats or opportunities** requiring monitoring and preparation. No immediate action required but strategic awareness is essential.

**Criteria:**
- Policy proposals at early consultation stage
- Narrative trends with upward trajectory
- Finance mechanisms under design
- Potential alliance opportunities

### 🟢 LOW
Signals that are **informational or favorable** to current positions. May represent coalition-building opportunities or positive narrative leverage.

**Criteria:**
- Third-party validations of Saudi sustainability commitments
- Alliance positions aligned with Arab Group
- Policy developments with neutral or positive impact

---

## Freshness System

| Badge | Age | Meaning |
|---|---|---|
| 🟢 **NEW** | ≤ 7 days | Breaking development — high priority review |
| 🟢 **RECENT** | 8–30 days | Active development — monitor closely |
| 🟡 **Xd AGO** | 31–90 days | Background context — situational awareness |
| 🔴 **STALE** | > 90 days | Historical reference only |

---

## Adding New Signals

Use `data/signal_template.json` as the base structure. Each signal requires:

```json
{
  "id": <unique integer>,
  "title": "Short descriptive title",
  "source": "Institution name",
  "risk": "High | Medium | Low",
  "category": "Narrative | Policy | Negotiation | Finance | Alliance | Strategic",
  "date": "daysAgo(N)  ← use the helper function",
  "summary": "2-3 sentence strategic summary",
  "link": "https://exact-page-url.org/specific-path",
  "linkLabel": "domain.org / Page Title",
  "linkNote": "Specific section or paragraph reference",
  "kw": ["keyword1", "keyword2", "keyword3"]
}
```

**Quality standards for signals:**
1. Link must point to the specific page, not a homepage
2. `linkNote` must identify the exact section where the signal is mentioned
3. Keywords should include technical terms, institution names, and policy concepts
4. Summary must include explicit reference to Saudi / Arab strategic implications
