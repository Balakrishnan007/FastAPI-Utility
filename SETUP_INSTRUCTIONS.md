# Setup Instructions

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Code editor of your choice
- Basic familiarity with REST APIs and data processing

## Quick Start

### 1. Environment Setup
```bash
# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Project Structure
Your final project should follow this structure:
```
utility-knowledge-api/
├── README.md                 # Your documentation
├── requirements.txt          # Dependencies
├── main.py                  # Application entry point (FastAPI skeleton provided)
├── data/                    # Sample data files (provided)
│   ├── equipment_inventory.csv
│   └── maintenance_logs.json
├── src/                     # Your source code
│   ├── __init__.py
│   ├── data_processor.py    # Data processing logic
│   ├── api.py              # API endpoints
│   └── models.py           # Data models (optional)
└── tests/                   # Your tests
    ├── __init__.py
    └── test_*.py           # Test files
```

### 3. Development Workflow

1. **Start with data exploration:**
   - Examine the sample CSV and JSON files
   - Understand the data structure and relationships

2. **Implement data processing:**
   - Create functions to load and parse the data files
   - Extract entities (equipment, locations, maintenance types)
   - Store data in appropriate data structures

3. **Build the API:**
   - Choose your web framework (FastAPI recommended for auto-docs)
   - Implement the required endpoints
   - Add proper error handling and validation

4. **Test your implementation:**
   - Write unit tests for key functions
   - Test API endpoints manually or with automated tests
   - Verify edge cases and error conditions

### 4. Running Your Application

We've provided a basic FastAPI skeleton in `main.py` to get you started:

```bash
# Run the FastAPI application
python main.py

# Or alternatively:
uvicorn main:app --reload
```

The application will start on `http://localhost:8000` with automatic API documentation at `/docs`.

### 5. Testing Your API

Use tools like:
- Browser for GET requests
- `curl` for command-line testing
- Postman for GUI-based testing
- Python `requests` library for automated testing

Example API calls:
```bash
# List all equipment
curl http://localhost:8000/api/equipment

# Search for specific equipment
curl http://localhost:8000/api/search?query=transformer

# Get maintenance logs
curl http://localhost:8000/api/maintenance
```

## Tips for Success

### Time Management (4 hours)
- **Hour 1:** Data exploration and basic processing
- **Hour 2:** Core API implementation  
- **Hour 3:** Error handling and testing
- **Hour 4:** Documentation and bonus features

### Common Pitfalls to Avoid
- Don't spend too much time on perfect code structure initially
- Start with core functionality before adding bonus features
- Test your API endpoints as you build them
- Don't forget to handle edge cases (empty files, invalid data)

### What We're Looking For
- **Working code** that can be run immediately
- **Clean, readable** implementation
- **Proper error handling** for edge cases
- **Good API design** following REST principles
- **Basic testing** of core functionality

### Getting Help
- Read the sample data files carefully
- Check the requirements.txt for available libraries
- Use the provided folder structure as a guide
- Remember: it's better to have working basic functionality than incomplete advanced features

## Submission Checklist
- [ ] Code runs without errors
- [ ] All core requirements implemented
- [ ] API endpoints respond correctly
- [ ] Basic error handling in place
- [ ] README with setup instructions
- [ ] At least one test file with meaningful tests
- [ ] Code is well-organized and readable

Good luck! Focus on demonstrating your problem-solving approach and Python fundamentals. 