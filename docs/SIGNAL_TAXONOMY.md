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
| 🟢 **NEW** | ≤ 7 days | Breaking development that is of high priority review |
| 🟢 **RECENT** | 8–30 days | Active development that needs to be monitored closely |
| 🟡 **Xd AGO** | 31–90 days | Background context serves as a situational awareness |
| 🔴 **STALE** | > 90 days | Historical reference only |

---

## Adding New Signals

New signals are added directly inside `index.html`. There is no separate form or admin panel (this will be revisted for improvement later just to enhance the security/protection of the `index.html`. The signals live in the JavaScript code as a list called `ALL_ALERTS`.

**Finding the right place in the file**
Open `index.html` in a text editor. Notepad works, but Notepad++ or Visual Studio Code are easier because they highlight the code structure and make it harder to introduce mistakes. Once the file is open, use Find (Ctrl+F) and search for `ALL_ALERTS`. This will jump you directly to the signal list.

Scroll to the bottom of the list. You will see the last signal entry ending with `}`, followed by a closing `]`;. Click just before that `]`; and paste your new signal entry there.

**Signal structure**
Use `data/signal_template.json` as the base structure. Each signal follows this format:

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
**Things to get right before saving**

The `id` must be a unique number not already used by another signal. Check the existing entries and pick the next number in sequence.
The `date` field uses `daysAgo(N)` rather than a hardcoded date. If the signal broke yesterday, use `daysAgo(1)`. If it was three days ago, use `daysAgo(3)`. This keeps the freshness badges accurate every time the file is opened.
The `link` should point to the specific page where the signal is reported, not the homepage of the institution. The `linkNote` should go one step further and identify the exact section or paragraph so a reader can find it without searching.
The `summary` should be written from a Saudi and Arab Group perspective, not just what happened, but why it matters strategically.

**After saving**

Save the file and open it in the browser to confirm the new signal appears. If the screen is blank or signals are not loading, the most common cause is a missing or extra comma. Check the entry immediately above where you added the new signal, it should end with `}`, not just `}`.

**Important Tip:**
Always save backup copy of the `index.html` to refer to it everytime you need to i.e., when you mess things up in it. 


**Quality standards for signals:**
1. Link must point to the specific page, not a homepage
2. `linkNote` must identify the exact section where the signal is mentioned
3. Keywords should include technical terms, institution names, and policy concepts
4. Summary must include explicit reference to Saudi / Arab strategic implications
