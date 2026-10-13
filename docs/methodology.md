# Statistical methodology and caveats

**Question:** Do Campaign A and Campaign B differ in mean stated purchase likelihood (1–7 rating)?

- H0: population mean A = population mean B.
- H1: population mean A ≠ population mean B.
- Two-sided pooled-variance independent-samples t-test, α = 0.05, matching the coursework analysis.
- The groups have 287 and 304 usable ratings respectively.
- Assumptions: independent observations, sufficiently reliable rating scale, and equal population variances for the pooled test. Random assignment and recruitment details were not established from the workbook.
- An ordinal 1–7 rating is analyzed as approximately interval-scaled, which should be acknowledged.
- The strong statistical difference is about survey responses, not conversion or revenue. Do not describe the results as conversion-rate uplift.
- As a sensitivity check, consider Welch's t-test because group sample variances differ. This repository reproduces the original pooled-variance approach.
