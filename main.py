"""
Utility Infrastructure Knowledge Extraction API

Main application entry point that sets up FastAPI and registers routes.
"""
import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.data_processor import load_equipment_data, load_maintenance_logs, validate_data_integrity
from src.api import root, get_equipment, get_maintenance, get_entities, search_data

# Application startup/shutdown handling
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handle application startup and shutdown."""
    print(" Starting application.")
    
    # Load data on startup
    equipment_loaded = load_equipment_data()
    maintenance_loaded = load_maintenance_logs()
    
    if equipment_loaded and maintenance_loaded:
        validation_issues = validate_data_integrity()
        if validation_issues:
            print(" Data validation issues found:")
            for issue in validation_issues:
                print(f"  - {issue}")
    
    print(" Application ready")
    yield
    print(" Application shutdown")

# Create FastAPI application
app = FastAPI(
    title="Utility Infrastructure Knowledge Extraction API",
    description="Process utility data and extract insights about equipment and maintenance",
    version="1.0.0",
    lifespan=lifespan
)

# Register API routes
app.get("/", summary="API Status")(root)
app.get("/api/equipment", summary="List Equipment")(get_equipment)
app.get("/api/maintenance", summary="List Maintenance Activities")(get_maintenance)
app.get("/api/entities", summary="Extract Key Entities")(get_entities)
app.get("/api/search", summary="Search Across Entities")(search_data)

# Run Application
if __name__ == "__main__":
    
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)