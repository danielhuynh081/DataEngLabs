# Data Engineering Labs – CS410

_Portland State University – Spring 2025_  
**Instructor:** Bruce Irvin  
**Author:** Daniel Huynh

---

## Project Overview

This repository contains lab work from the **CS410: Data Engineering** course at PSU. Each lab focuses on essential topics in data profiling, validation, transformation, storage, and integration.

---

## Labs Breakdown

### Lab1 - Data Gathering

Explored and profiled raw datasets to understand structure, quality, and initial cleaning needs.

### Lab2 - Data Transport

Created validation assertions to ensure integrity and correctness across records.

### Lab3 - Data Validation

Checked for nulls, logical errors, invalid ranges, and referential mismatches across employee data.

### Lab4 - Data Transformation

Standardized inconsistent entries and cleaned up real-world messy datasets using Pandas.

### Lab5 - Data Storage

Designed relational schemas, loaded data using `psycopg2`, and built indexes for optimized querying.

### Lab6 - Data Integration

Joined COVID-19 and Census datasets by creating composite keys, then performed correlation analysis.

---

## Tools & Technologies

- Python (Pandas, Matplotlib, Seaborn)
- PostgreSQL
- Jupyter Notebooks
- Git & GitHub

---

## Key Takeaways

- Data quality matters: catching issues early with validation assertions.
- Speed and structure: leveraging bulk imports and indexes for performance.
- Schema design: modeling data for scalability and query efficiency.
- Real-world integration: joining noisy datasets with inconsistent keys.
- Analytical insight: using correlation matrices to uncover meaningful patterns.

---

## Project Structure

```plaintext
DataEngLabs/
├── Lab1 - Data Gathering/
├── Lab2 - Data Transport/
├── Lab3 - Data Validation/
├── Lab4 - Data Transformation/
├── Lab5 - Data Storage/
├── Lab6 - Data Integration/
└── README.md
```
