"""Analyze A/B purchase-likelihood survey (1–7 scale)."""
from pathlib import Path
import csv
import math
import statistics
from scipy import stats
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
with (ROOT / "data/purchase_likelihood.csv").open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
groups = {g: [int(r["purchase_likelihood"]) for r in rows if r["campaign"] == g] for g in ("A", "B")}
a, b = groups["A"], groups["B"]
if not a or not b or any(v not in range(1, 8) for v in a+b):
    raise ValueError("Expected valid campaign A/B responses on a 1–7 scale")
na, nb = len(a), len(b)
ma, mb = statistics.mean(a), statistics.mean(b)
va, vb = statistics.variance(a), statistics.variance(b)
pooled = ((na-1)*va + (nb-1)*vb) / (na+nb-2)
se = math.sqrt(pooled*(1/na+1/nb))
t = (mb-ma)/se
df = na+nb-2
p = 2*stats.t.sf(abs(t), df)
critical = stats.t.ppf(.975, df)
lo, hi = (mb-ma)-critical*se, (mb-ma)+critical*se
print(f"A: n={na}, mean={ma:.4f}, sd={math.sqrt(va):.4f}")
print(f"B: n={nb}, mean={mb:.4f}, sd={math.sqrt(vb):.4f}")
print(f"Difference (B-A)={mb-ma:.4f}; t({df})={t:.4f}; p={p:.4e}; 95% CI=({lo:.4f}, {hi:.4f})")
fig, ax = plt.subplots(figsize=(7, 4.5))
ax.bar(["Campaign A", "Campaign B"], [ma, mb], yerr=[1.96*math.sqrt(va/na), 1.96*math.sqrt(vb/nb)], capsize=6)
ax.set_ylim(0, 7); ax.set_ylabel("Mean purchase likelihood (1–7)")
ax.set_title("Campaign purchase-likelihood comparison")
fig.tight_layout()
(ROOT / "figures").mkdir(exist_ok=True)
fig.savefig(ROOT / "figures/campaign_comparison.png", dpi=180)
