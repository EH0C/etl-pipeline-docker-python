# ETL Pipeline with Docker, Python & Crontab

**An end-to-end ETL pipeline** that extracts data from a **MariaDB source**, transforms it using **Python**, and loads it into a **MariaDB data warehouse**. Fully containerized and automated with **Docker Compose** and **Cron**. Includes **anonymized/synthetic sample data** for demonstration.

## Key Features

* Containerized ETL workflow using **Docker Compose**
* Automated scheduled ETL with **Cron**
* Data extraction from MariaDB
* Data transformation using **Python (Pandas + SQLAlchemy)**
* Loading transformed data into a MariaDB warehouse
* Self-contained demo environment

## Architecture Overview

```
Source MariaDB  -->  Python ETL Job  -->  Target MariaDB DW
  (sample data)      (script.py)          (data warehouse)
```

Automated via Cron inside the Python container.

## Quick Start

### Prerequisites

* Docker & Docker Compose
* Basic knowledge of SQL and Python

### Setup

```bash
git clone https://github.com/yourusername/etl-docker-cron.git
cd etl-docker-cron
docker-compose up --build -d
```

* `source_mariadb` → Sample database
* `target_mariadb` → Warehouse
* `etl_cron` → Python ETL container running Cron

### Run ETL Manually

```bash
docker exec -it etl_cron python /app/script.py
```

ETL runs automatically according to the Cron schedule inside the container.

## 📂 Project Structure

```
etl-docker-cron/
│
├─ script.py            # Main ETL script
├─ Dockerfile           # Python container with cron
├─ crontab              # Cron schedule file
├─ docker-compose.yaml  # Docker Compose setup
├─ requirements.txt     # Python dependencies
└─ sample_data/         # Sample data for demonstration
```

## Dependencies

* Python 3.11
* pandas
* SQLAlchemy
* pymysql

All installed via `requirements.txt` during container build.

## Customization

* **Database credentials** → Update `docker-compose.yaml`
* **Cron schedule** → Modify `crontab` file
* **Transformations** → Customize logic in `script.py`

---
