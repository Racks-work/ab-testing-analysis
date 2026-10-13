-- PostgreSQL: import data/purchase_likelihood.csv into this table using pgAdmin Import/Export.
CREATE TABLE IF NOT EXISTS purchase_likelihood (
  campaign TEXT NOT NULL CHECK (campaign IN ('A','B')),
  purchase_likelihood INTEGER NOT NULL CHECK (purchase_likelihood BETWEEN 1 AND 7)
);
-- In psql (run from the repository root):
-- \copy purchase_likelihood(campaign,purchase_likelihood) FROM 'data/purchase_likelihood.csv' WITH (FORMAT csv, HEADER true);

SELECT campaign, COUNT(*) AS responses,
       ROUND(AVG(purchase_likelihood),4) AS mean_likelihood,
       ROUND(STDDEV_SAMP(purchase_likelihood),4) AS sample_sd,
       ROUND(VAR_SAMP(purchase_likelihood),4) AS sample_variance
FROM purchase_likelihood
GROUP BY campaign ORDER BY campaign;

WITH stats AS (
 SELECT campaign, COUNT(*)::numeric AS n, AVG(purchase_likelihood) AS mean,
        VAR_SAMP(purchase_likelihood) AS variance
 FROM purchase_likelihood GROUP BY campaign
), paired AS (
 SELECT a.n AS na,b.n AS nb,a.mean AS ma,b.mean AS mb,
        ((a.n-1)*a.variance+(b.n-1)*b.variance)/(a.n+b.n-2) AS pooled_var
 FROM stats a CROSS JOIN stats b WHERE a.campaign='A' AND b.campaign='B'
)
SELECT ROUND((mb-ma)::numeric,4) AS mean_difference_b_minus_a,
       ROUND(((mb-ma)/SQRT(pooled_var*(1/na+1/nb)))::numeric,4) AS pooled_t_statistic,
       (na+nb-2)::integer AS degrees_of_freedom
FROM paired;
-- For an exact two-sided p-value and confidence interval, run python/analyze.py (SciPy).
