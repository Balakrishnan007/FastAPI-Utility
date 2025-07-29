# Utility Infrastructure Knowledge Extraction API

A FastAPI-based REST API for processing and querying utility equipment and maintenance data.  
The API ingests CSV and JSON files, extracts key entities, and provides endpoints for search, filtering, and relationship mapping.  
This project demonstrates backend development with FastAPI, focusing on structured data processing, entity extraction, and automated testing.

## Features

- Ingest and process CSV (equipment) and JSON (maintenance) datasets
- Entity extraction: equipment types, locations, maintenance types, manufacturers, and technicians
- REST API with five endpoints
- Search and filtering capabilities
- Automatic interactive API documentation with Swagger UI
- Unit and API tests using pytest
- Basic entity relationship mapping
- Simple in-memory data storage for ease of use

## Setup Instructions

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Balakrishnan007/FastAPI-Utility.git
   cd FastAPI-Utility


2. Create and activate virtual environment
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies
   ```
   pip install -r requirements.txt
   ```

4. Verify data files exist
   - `data/equipment_inventory.csv`
   - `data/maintenance_logs.json`

### Running the Application

1. Start the server
   ```
   python main.py
   ```

2. Verify it's working
   - Open browser: `http://localhost:8000`
   - API Documentation: `http://localhost:8000/docs`

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Health check and API status |
| `/api/equipment` | GET | List equipment with optional filters |
| `/api/maintenance` | GET | List maintenance activities with filters |
| `/api/entities` | GET | Extract all key entities from data |
| `/api/search` | GET | Search across all data |

### Usage Examples

```
# Health check
curl http://localhost:8000/

# Get all equipment
curl http://localhost:8000/api/equipment

# Filter equipment by type
curl "http://localhost:8000/api/equipment?equipment_type=Transformer"

# Search functionality
curl "http://localhost:8000/api/search?query=transformer"
```

## Running Tests

```
# Install test dependencies if needed
pip install pytest httpx

# Run tests
pytest tests/test.py -v
```

## Project Structure

```
FastAPI-Utility/
├── README.md
├── requirements.txt
├── main.py                  # Application entry point
├── data/                    # Sample data files
│   ├── equipment_inventory.csv
│   └── maintenance_logs.json
├── src/                     # Source code
│   ├── data_processor.py    # Data processing logic
│   └── api.py              # API endpoints
└── tests/                   # Tests
    └── test.py
```

## Technology Stack

- FastAPI - Web framework
- Uvicorn - ASGI server
- Pytest - Testing framework
- Python 3.10+

## Troubleshooting

### Application won't start
- Check Python version: `python --version`
- Verify data files exist in `data/` folder
- Install dependencies: `pip install -r requirements.txt`

### Tests failing
- Install test dependencies: `pip install pytest httpx`
- Run from project root directory

### Port already in use
- Kill any existing processes on port 8000
- Or change port in main.py

