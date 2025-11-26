
---

# End-to-End ETL Pipeline with Docker, Python, and Crontab

This project demonstrates an **end-to-end ETL (Extract, Transform, Load) pipeline** using **Docker Compose**, **Python**, and **Crontab**. It extracts data from a **MariaDB source database**, applies **transformations**, and loads it into a **final MariaDB data warehouse**. The repository includes **anonymized/synthetic sample data** for demonstration purposes.

---

## Features

* Fully containerized ETL workflow using Docker Compose.
* Automated ETL execution using Cron inside a Python container.
* Extraction from a MariaDB source database.
* Data transformation using Python (Pandas/SQLAlchemy).
* Load transformed data into a MariaDB warehouse.
* Self-contained demo with sample data—no external database needed.

---

## Architecture Overview

```
+------------------+      +------------------+      +---------------------+
|                  |      |                  |      |                     |
|  Source MariaDB  | ---> |  Python ETL Job  | ---> |  Target MariaDB DW  |
|  (synth. sample) |      |  (script.py)     |      |                     |
+------------------+      +------------------+      +---------------------+
        ^                        |
        |                        |
      Docker Compose             Crontab
        |
      Containers
```

**Workflow:**

1. **Extract**: Pull data from the source MariaDB container.
2. **Transform**: Apply transformations in Python (e.g., rename columns, type conversion, data cleaning).
3. **Load**: Insert transformed data into the target MariaDB warehouse.
4. **Automate**: Run the ETL script at scheduled intervals via Cron.

---

## Getting Started

### Prerequisites

* [Docker](https://www.docker.com/products/docker-desktop)
* [Docker Compose](https://docs.docker.com/compose/)
* Python 3.11+ (inside container)
* Basic knowledge of SQL and Python

---

### Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/etl-docker-cron.git
cd etl-docker-cron
```

2. Build and start the Docker containers:

```bash
docker-compose up --build -d
```

This will start:

* `source_mariadb` → Sample MariaDB database
* `target_mariadb` → Data warehouse
* `etl_cron` → Python ETL container running cron

---

### Run ETL Manually

Inside the Python ETL container:

```bash
docker exec -it etl_cron python /app/script.py
```

---

### Automated ETL

The ETL script is set up to run automatically according to the schedule defined in the Crontab inside the container.

---

## Project Structure

```
etl-docker-cron/
│
├─ script.py            # Main ETL script
├─ Dockerfile           # Python ETL container with cron
├─ crontab              # Cron schedule file
├─ docker-compose.yaml  # Defines all containers
├─ requirements.txt     # Python dependencies
└─  sample_data/         # Anonymized source data
```

---

## Customization

* **Database credentials**: Update environment variables in `docker-compose.yaml`.
* **Cron schedule**: Modify `/etc/crontabs/root` inside the Python container or the `crontab` file.
* **Transformations**: Edit `script.py` to include your data cleaning, type conversion, and business logic.

---

## Dependencies

* Python 3.11
* pandas
* SQLAlchemy
* pymysql

These are installed automatically via `requirements.txt` during container build.

---

