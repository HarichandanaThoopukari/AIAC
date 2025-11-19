import sqlite3
from pprint import pprint


def setup_database(connection: sqlite3.Connection) -> None:
    cursor = connection.cursor()
    cursor.executescript(
        """
        DROP TABLE IF EXISTS Bills;
        DROP TABLE IF EXISTS Services;
        DROP TABLE IF EXISTS Patients;

        CREATE TABLE Patients (
            patient_id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            date_of_birth DATE NOT NULL,
            phone_number TEXT NOT NULL,Q
            insurance_provider
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        [
            (1, "Alice", "Nguyen", "1987-06-22", "555-0100", "HealthGuard"),
            (2, "Brian", "Lopez", "1993-11-04", "555-0111", "MediPrime"),
            (3, "Chloe", "Bennett", "1979-02-15", "555-0122", "CareTrust"),
        ],
    )
    cursor.executemany(
        """
        INSERT INTO Services (
            service_id,
            service_name,
            service_description,
            unit_cost
        )
        VALUES (?, ?, ?, ?)
        """,
        [
            (1, "General Consultation", "Routine physician visit", 80.00),
            (2, "MRI Scan", "Magnetic resonance imaging", 1200.00),
            (3, "Blood Test Panel", "Comprehensive lab panel", 220.00),
            (4, "Physical Therapy", "Post-operative PT session", 150.00),
        ],
    )
    cursor.executemany(
        """
        INSERT INTO Bills (
            bill_id,
            patient_id,
            service_id,
            service_date,
            quantity,
            discount_pct,
            tax_pct,
            notes
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        [
            (1001, 1, 1, "2025-11-01", 1, 0.00, 0.07, "Initial consult"),
            (1002, 1, 3, "2025-11-02", 1, 0.10, 0.07, "Lab work"),
            (1003, 2, 2, "2025-11-03", 1, 0.05, 0.07, "MRI for knee"),
            (1004, 2, 1, "2025-11-04", 2, 0.00, 0.07, "Follow-up consults"),
            (1005, 3, 4, "2025-11-05", 6, 0.15, 0.07, "Rehab sessions"),
        ],
    )
    connection.commit()


def fetch_patient_totals(connection: sqlite3.Connection):
    cursor = connection.cursor()
    cursor.execute(
        """
        WITH BillLine AS (
            SELECT
                b.bill_id,
                b.patient_id,
                p.first_name,
                p.last_name,
                s.service_name,
                b.quantity,
                s.unit_cost,
                b.discount_pct,
                b.tax_pct,
                (b.quantity * s.unit_cost) AS gross_amount,
                (b.quantity * s.unit_cost) * (1 - b.discount_pct) AS discounted_amount,
                (b.quantity * s.unit_cost) * (1 - b.discount_pct) * (1 + b.tax_pct) AS line_total
            FROM Bills b
            JOIN Patients p ON p.patient_id = b.patient_id
            JOIN Services s ON s.service_id = b.service_id
        )
        SELECT
            patient_id,
            first_name,
            last_name,
            ROUND(SUM(gross_amount), 2) AS total_before_discounts,
            ROUND(SUM(discounted_amount), 2) AS total_after_discounts,
            ROUND(SUM(line_total), 2) AS total_bill_due
        FROM BillLine
        GROUP BY patient_id, first_name, last_name
        ORDER BY last_name, first_name
        """
    )
    return cursor.fetchall()


def main():
    with sqlite3.connect(":memory:") as conn:
        setup_database(conn)
        totals = fetch_patient_totals(conn)
    print("Patient billing totals:")
    pprint(totals)


if __name__ == "__main__":
    main()

