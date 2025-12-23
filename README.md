# Semester Project — End-to-End CRUD Application

**Course:** Database Systems (AI Specialization, PUT)

**Instructor:** Dr. Serhii Baraban

**Delivery:** Individual 

**Repository:** GitHub Classroom 

## Goal

Design and implement a small information system from scratch that:

1. starts with clear **business rules** and **data modeling**
2. results in a **normalized relational schema** with constraints and sample data
3. exposes **full CRUD** via a simple **user interface** (web or APEX/Appsmith)
4. demonstrates **basic DB engineering**: keys, FKs, indexes, views.

---

## Milestones & Deliverables

> Use the repo structure below; each milestone is a Pull Request(PR) with a short report in `README.md`.

### M1 — Problem Definition & Business Rules 

* Domain selection + **user stories** 
* **Business rules** (cardinalities, optionality, constraints)
* `docs/BRIEF.md` (≤2 pages)

### M2 — Conceptual Modeling 

* **Crow’s Foot ERD** (entities, attributes, PK/FK, M:N resolved)
* **UML Class Diagram** (multiplicities + inheritance if used)
* Rationale for design decisions
* `diagrams/ERD.png`, `diagrams/UML.png`, `docs/M2_NOTES.md`

### M3 — Logical/Physical Design 

* **Relational schema** (CREATE TABLE …), PK/FK, CHECK, UNIQUE, NOT NULL
* At least **1 M:N** relationship resolved via a bridge table
* **Indexes**: ≥2 purposeful (e.g., lookup + FK side)
* **Views**: ≥1 for read-only reporting
* **Sample data**: ≥50 rows across tables (SQL seed or CSV)
* `sql/schema.sql`, `sql/seed.sql`, `sql/views.sql`, `sql/indexes.sql`

### M4 — Data Access Layer & API 

Pick one track:

* **Track A (Low-code):** Oracle **APEX** or **Appsmith**

  * Pages/widgets that cover **Create, Read (listing + detail), Update, Delete**
  * Use **bind variables/parameters** or prepared queries
  * Authentication (APEX built-in or Appsmith simple auth)

* **Track B (Code-first):** Minimal **web app**

  * Recommended stacks:

    * Python **Flask**/**FastAPI** + PostgreSQL
    * Node **Express** + PostgreSQL
    * Java **Spring Boot** + PostgreSQL
  * **REST endpoints** for main entities (GET/POST/PUT/DELETE)
  * Use **prepared statements/ORM** (SQLAlchemy/Prisma/JPA)
  
### M5 — User Interface 

* UI covering **all CRUD** paths for at least **two core entities**
* Create/Update forms 
* Detail view that shows **1:N** child rows (e.g., order items of an order)
* Screenshots: `docs/ui/…`

### Final — Demo & Report 

* 5 minute demo (video or live) 
* Final **README** with setup steps, ERD/UML images, and reflections

---

## Functional Requirements 

1. ≥ **3 entities**, incl. one **M:N** resolved by a bridge table
2. Full **CRUD** for 2 core entities via UI
3. **List, search, paginate** (optional)
4. **Detail** page with related rows (1:N)
5. **Indexes** that matter (prove with EXPLAIN/ANALYZE or APEX/EXPLAIN)
6. ≥ **1 VIEW** used in UI/report
7. **Seed data** and **reproducible setup** (SQL scripts)

---

## Non-functional Requirements

* Clear **README** 
* Consistent naming (`snake_case` tables/columns)
* **Git hygiene**: small commits with messages, issues/Project board optional

---

## Repository Structure

```
/ (repo root)
├─ README.md
├─ docs/
│  ├─ BRIEF.md
│  ├─ M2_NOTES.md
│  ├─ perf.md
│  └─ ui/ (screenshots)
├─ diagrams/
│  ├─ ERD.png
│  └─ UML.png
├─ sql/
│  ├─ schema.sql
│  ├─ seed.sql
│  ├─ indexes.sql
│  └─ views.sql
├─ app/               
```

---

## Domain Ideas (choose one or propose your own)

see the docs/project_semester_variants.xlsx

---

## Grading Rubric

### Grading Policy
- **Grade 4 (Good):** Database-related milestones M1–M3 completed, verified in PostgreSQL.
  - Includes: ERD ✓  schema.sql ✓  seed.sql ✓  views ✓  indexes 
  - API/UI components may be omitted.

- **Grade 5 (Very Good):** All database-related milestones M1–M5 completed
  - Implemented Data Access Layer or REST API (Flask/FastAPI),
  - Working UI and demonstration of CRUD operations.
  - Documentation updated.

---

## Technology Options

* **DB:** PostgreSQL (preferred), Oracle (APEX track allowed)
* **Low-code:** Oracle **APEX** or **Appsmith**
* **Code-first:**

  * Python **Flask/FastAPI** (+ SQLAlchemy/psycopg)
  * Node **Express** (+ Prisma/pg)
  * Java **Spring Boot** (+ JPA/Hibernate)

> Whatever you choose, **use prepared statements/ORM** to avoid SQL injection.

---

## Academic Integrity & AI Use

* You may use AI tools (ChatGPT/Copilot) as **assistants**, not as authors.
* You must **review, test, and cite** AI-generated snippets in `README.md` (“AI assistance used for X; verified by Y”).
* Plagiarism or identical repos → zero.

---

## Submission

* Push code & artifacts to your Classroom repo.
* Ensure `sql/` scripts rebuild DB from scratch.

---

