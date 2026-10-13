# ab-testing-analysis[README.md](https://github.com/user-attachments/files/33404455/README.md)
# A/B Testing: Campaign Purchase Likelihood

A reproducible statistical analysis of survey responses for Campaign A versus Campaign B, drawn from a Chapter 6 coursework dataset. Ratings measure **stated purchase likelihood (1 = very unlikely, 7 = very likely)**, **not observed conversions**.

## Key findings

| Metric | A | B |
|---|---:|---:|
| Responses | 287 | 304 |
| Mean rating | 2.4948 | 3.9178 |
| Sample variance | 1.1739 | 0.6698 |

- Difference in means (B − A): **1.4230 points**
- Two-sided, pooled-variance t-test: **t(589) = 18.0790** (B − A convention)
- **p ≈ 1.91 × 10⁻⁵⁸**; reject equal-means null hypothesis at α = 0.05
- 95% confidence interval for B − A: **[1.2684, 1.5776]**

**Interpretation:** Respondents rated Campaign B more favorably on purchase likelihood. This does not establish an increase in actual purchases, and causal claims require confirmation of random assignment and study design.

## Repository structure

- `data/purchase_likelihood.csv`: 591 anonymized survey ratings derived from the prior coursework workbook
- `python/analyze.py`: reproducible statistics and chart generation
- `python/requirements.txt`: Python dependencies
- `sql/analysis.sql`: PostgreSQL group summaries and pooled t statistic
- `docs/methodology.md`: assumptions and limitations
- `figures/`: generated plot output location

## Run the Python analysis

```bash
python -m pip install -r python/requirements.txt
python python/analyze.py
```

The script prints sample statistics, two-sided p-value and 95% CI, and writes `figures/campaign_comparison.png`.

## Run the SQL

Create a PostgreSQL database, run `sql/analysis.sql` to create the table, import `data/purchase_likelihood.csv` using pgAdmin's **Import/Export Data** (CSV with header), then rerun the SELECT queries. The commented `\copy` command works in `psql`, not the pgAdmin Query Tool.

## Methods

Independent-samples two-sided pooled-variance t-test; α = 0.05. See `docs/methodology.md`. Python computes the p-value using SciPy; SQL computes descriptive statistics and the t statistic.

## Attribution

Adapted from a student A/B testing coursework workbook. Confirm course and dataset redistribution permissions before making the raw data public. Code and narrative were prepared for portfolio presentation; review them and verify execution in your own environment.
