# Utility Infrastructure Knowledge Extraction API

## Background
You are building a system for a utility company that needs to digitize and extract knowledge from various infrastructure reports and maintenance logs. The goal is to create a simple API that can process utility data and provide insights about equipment, locations, and maintenance activities.

## Your Task (4 hours)
Build a Python application that:

1. **Processes utility infrastructure data** from JSON and CSV files
2. **Extracts key entities** (equipment types, locations, maintenance activities)
3. **Provides a REST API** to query the processed information
4. **Implements basic knowledge relationships** between entities

## Project Requirements

### Core Features (Must Have)
- [ ] Data ingestion from provided sample files (CSV and JSON)
- [ ] Entity extraction (equipment, locations, maintenance types)
- [ ] REST API with at least 3 endpoints
- [ ] Basic data validation and error handling
- [ ] Simple in-memory storage for processed data (no database required; you can work directly on files)

### Bonus Features (Nice to Have)
- [ ] One unit test for one core function
- [ ] API documentation (e.g., with FastAPI auto-docs)
- [ ] Basic entity relationship mapping
- [ ] Data export functionality
- [ ] Simple search/filtering capabilities

### Technical Requirements
- Python 3.8+
- Any web framework (FastAPI, Flask, etc.)
- Standard libraries preferred, minimal external dependencies
- Clean, readable code with comments
- Follow Python naming conventions

## Evaluation Criteria

### Code Quality (40%)
- Clean, readable, and well-organized code
- Proper error handling
- Meaningful variable/function names
- Code documentation

### Functionality (40%)
- Meets core requirements
- API works as expected
- Handles edge cases appropriately
- Data processing is accurate

### Problem Solving (20%)
- Logical approach to the problem
- Efficient algorithms and data structures
- Creative solutions to challenges

## Getting Started

1. Review the sample data in the `data/` directory
2. Set up your development environment (see `SETUP_INSTRUCTIONS.md`)
3. Start with the provided FastAPI skeleton in `main.py`
4. Implement the core features step by step
5. Test your API endpoints
6. Document any assumptions or design decisions

## Sample API Endpoints (Suggested)

```
GET /api/equipment - List all equipment
GET /api/locations - List all locations  
GET /api/maintenance - List maintenance activities
POST /api/process - Process new data file
GET /api/search?query=... - Search across entities
```

## Submission

Please provide:
- Complete source code
- README with setup instructions
- Brief explanation of your design decisions
- Any assumptions you made

Good luck! 