# Autoria Project Structure

This document provides an overview of the directory structure and the responsibilities of each component within the Autoria project.

# Directory Descriptions

| Directory | Purpose |
| :--- | :--- |
| **`docker/`** | Contains **Docker-related files** (e.g., `Dockerfile`, `docker-compose.yml`) for environment setup and containerization. |
| **`dumps/`** | Storage for **database dump files** (initial data, backups, or fixture data). |
| **`src/`** | The main application source code directory. |
| **`src/db/`** | Handles **database connection setup** and initialization logic. |
| **`src/migration/`** | Stores **database migration scripts** (e.g., using Alembic or similar tools) to manage schema changes. |
| **`src/models/`** | Defines the **ORM models** (e.g., SQLAlchemy models) that represent the database schema. |
| **`src/schemas/`** | Contains Data Transfer Objects (DTOs) used for data validation and serialization/deserialization across application. |
| **`src/repositories/`** | The **Data Access Layer**. Encapsulates logic for querying and persisting data to and from the database. |
| **`src/scraper/`** | Holds the dedicated **web scraping logic** and components. |
| **`src/tasks/`** | Defines **scheduled/background tasks** (e.g., using Celery or similar) for asynchronous and long-running operations (like the scraper). |
| **`src/utils/`** | A collection of **helper functions and utilities** that are generic and reusable across different parts of the application. |

# Run Autoria Parser

The core operational times for the scraper and database maintenance are managed via environment variables in the /docker/.env-docker file:
- **SCRAPER_RUN_TIME**=13:00
- **DUMP_RUN_TIME**=13:00

**To run** the application execute the following command from the root directory:
- ```docker compose -f ./docker/docker-compose.yaml up```
