# SE 202 W7 — Object-Relational Mapping

Contains starter implementations for tasks 0–14 in `python-object_relational_mapping`.

## Notes
- Tasks 0–5 use `MySQLdb`.
- Task 2 intentionally uses `.format()` because that is what the exercise asks you to demonstrate; it is vulnerable to SQL injection by design.
- Task 3 uses parameterized SQL and is safe against SQL injection.
- Tasks 6–14 use SQLAlchemy.
- Configure MySQL credentials and ensure the required databases/tables exist before running scripts.
- Task 11 inserts a new Louisiana row every time it runs; use a clean test database or check for duplicates.
