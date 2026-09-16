# Log Processing Pipeline

A Python-based log processing pipeline that parses raw log files, validates records, performs aggregations, and loads results into PostgreSQL.

## Input Log Format

Example:

2024-01-01 10:00:00 {"user_id": 1, "event": "click", "page": "home"}

## Project Structure

log_pipeline/

├── src/

│   ├── parser.py

│   ├── normalizer.py

│   ├── validator.py

│   ├── pipeline.py

│   └── aggregator.py

│

├── data/

│   └── sample_logs.txt

│

├── main.py

├── requirements.txt

├── .gitignore

└── README.md

## Features

* Parse JSON log records
* Normalize incoming data
* Validate click events
* Remove duplicate records
* Aggregate metrics
* Export results to PostgreSQL

## Metrics Implemented

* Clicks per page
* Unique users per page
* Clicks per hour
* Top N pages by clicks
* Top N users by activity
* Clicks and unique users per page
* Page-wise clicks per hour
* User activity summary

## PostgreSQL Output

Aggregated results are loaded into PostgreSQL using Pandas and SQLAlchemy.

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd log_pipeline
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a PostgreSQL database

```sql
CREATE DATABASE log_pipeline;
```

### 5. Create a `.env` file

```env
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=log_pipeline
```

### 6. Add input log file

Place the log file in the `data/` directory.

### 7. Run the pipeline

```bash
python main.py
```

## requirements.txt

pandas

sqlalchemy

psycopg2-binary

python-dotenv
