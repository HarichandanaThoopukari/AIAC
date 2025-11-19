# Hospital Billing Example

Files:
- `hospital_billing.sql` - SQL schema and sample data for Patients, Services, Bills.
- `run_billing.py` - Python script that loads the SQL into an in-memory SQLite DB and prints total bill per patient and line items.

How to run:

Make sure you have Python 3 installed. From the workspace directory run:

```powershell
python .\run_billing.py
```

What it shows:
- Totals per patient using a JOIN and SUM over service cost * quantity.
- Detailed per-service billed lines.

SQL example to compute totals (shown in `hospital_billing.sql`):

```sql
SELECT p.id, p.name, SUM(s.cost * b.quantity) AS total_bill
FROM Bills b
JOIN Patients p ON b.patient_id = p.id
JOIN Services s ON b.service_id = s.service_id
GROUP BY p.id, p.name;
```
