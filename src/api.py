"""
API endpoints for the Utility Infrastructure Knowledge Extraction API.

This module contains all the FastAPI route definitions.
"""

from typing import Optional
from fastapi import HTTPException, Query
from src.data_processor import (
    get_equipment_data, 
    get_maintenance_logs, 
    extract_entities, 
    validate_data_integrity
)

async def root():
    """Get API status and data summary."""
    equipment_data = get_equipment_data()
    maintenance_logs = get_maintenance_logs()
    validation_issues = validate_data_integrity()
    
    return {
        "api": "Utility Infrastructure Knowledge Extraction API",
        "version": "1.0.0",
        "status": "healthy" if not validation_issues else "issues_detected",
        "data_summary": {
            "equipment_count": len(equipment_data),
            "maintenance_count": len(maintenance_logs),
            "validation_issues": len(validation_issues)
        },
        "endpoints": [
            "GET /api/equipment - List equipment with filters",
            "GET /api/maintenance - List maintenance with filters",
            "GET /api/entities - Extract key entities",
            "GET /api/search - Search across all data"
        ]
    }

async def get_equipment(
    equipment_type: Optional[str] = Query(None, description="Filter by equipment type"),
    status: Optional[str] = Query(None, description="Filter by status")
):
    """Get equipment list with basic filtering."""
    try:
        equipment_data = get_equipment_data()
        if not equipment_data:
            raise HTTPException(status_code=503, detail="Equipment data not available")
        
        result = equipment_data.copy()
        
        # Apply basic filters
        if equipment_type:
            result = [eq for eq in result 
                     if eq.get("equipment_type", "").lower() == equipment_type.lower()]
        
        if status:
            result = [eq for eq in result 
                     if eq.get("status", "").lower() == status.lower()]
        
        return {
            "count": len(result),
            "equipment": result
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving equipment: {str(e)}")

async def get_maintenance(
    equipment_id: Optional[str] = Query(None, description="Filter by equipment ID"),
    status: Optional[str] = Query(None, description="Filter by status")
):
    """Get maintenance activities with basic filtering."""
    try:
        maintenance_logs = get_maintenance_logs()
        if not maintenance_logs:
            raise HTTPException(status_code=503, detail="Maintenance data not available")
        
        result = maintenance_logs.copy()
        
        # Apply basic filters
        if equipment_id:
            result = [log for log in result if log.get("equipment_id") == equipment_id]
        
        if status:
            result = [log for log in result 
                     if log.get("status", "").lower() == status.lower()]
        
        return {
            "count": len(result),
            "maintenance": result
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving maintenance: {str(e)}")

async def get_entities():
    """Extract and return key entities from the data."""
    try:
        equipment_data = get_equipment_data()
        maintenance_logs = get_maintenance_logs()
        
        if not equipment_data and not maintenance_logs:
            raise HTTPException(status_code=503, detail="No data available")
        
        entities = extract_entities()
        
        return {
            "entities": entities,
            "summary": {
                "equipment_types": len(entities["equipment_types"]),
                "locations": len(entities["locations"]),
                "maintenance_types": len(entities["maintenance_types"]),
                "manufacturers": len(entities["manufacturers"]),
                "technicians": len(entities["technicians"]),
                "total_unique_entities": sum(len(v) for v in entities.values())
            }
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error extracting entities: {str(e)}")

async def search_data(query: str = Query(..., description="Search query")):
    """Search across all entities and data."""
    try:
        if not query.strip():
            raise HTTPException(status_code=400, detail="Search query cannot be empty")
        
        equipment_data = get_equipment_data()
        maintenance_logs = get_maintenance_logs()
        
        query_lower = query.lower()
        results = {
            "equipment": [],
            "maintenance": []
        }
        
        # Search equipment data
        for equipment in equipment_data:
            searchable_text = " ".join([
                equipment.get("equipment_id", ""),
                equipment.get("equipment_type", ""),
                equipment.get("location", ""),
                equipment.get("manufacturer", ""),
                equipment.get("model", ""),
                equipment.get("status", "")
            ]).lower()
            
            if query_lower in searchable_text:
                results["equipment"].append(equipment)
        
        # Search maintenance data
        for log in maintenance_logs:
            searchable_text = " ".join([
                log.get("log_id", ""),
                log.get("equipment_id", ""),
                log.get("maintenance_type", ""),
                log.get("technician", ""),
                log.get("description", ""),
                log.get("status", "")
            ]).lower()
            
            if query_lower in searchable_text:
                results["maintenance"].append(log)
        
        return {
            "query": query,
            "total_results": len(results["equipment"]) + len(results["maintenance"]),
            "results": results
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error performing search: {str(e)}")