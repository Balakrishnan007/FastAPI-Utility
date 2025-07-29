"""
Data processing logic for the Utility Infrastructure API.

This module contains functions for loading, processing, and analyzing
utility equipment and maintenance data.
"""

import csv
import json
from pathlib import Path
from typing import Dict, List, Any

# Global storage for processed data
equipment_data = []
maintenance_logs = []

def load_equipment_data():
    """Load and process equipment data from CSV file."""
    global equipment_data
    filepath = Path("data/equipment_inventory.csv")
    
    try:
        with filepath.open("r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            equipment_data = list(reader)
        print(f" Loaded {len(equipment_data)} equipment records")
        return True
    except FileNotFoundError:
        print(" Equipment CSV not found")
        equipment_data = []
        return False
    except Exception as e:
        print(f" Error loading equipment: {e}")
        equipment_data = []
        return False

def load_maintenance_logs():
    """Load and process maintenance data from JSON file."""
    global maintenance_logs
    filepath = Path("data/maintenance_logs.json")
    
    try:
        with filepath.open("r", encoding="utf-8") as f:
            maintenance_logs = json.load(f)
        print(f" Loaded {len(maintenance_logs)} maintenance records")
        return True
    except FileNotFoundError:
        print(" Maintenance JSON not found")
        maintenance_logs = []
        return False
    except Exception as e:
        print(f" Error loading maintenance: {e}")
        maintenance_logs = []
        return False

def extract_entities():
    """Extract key entities from both datasets."""
    entities = {
        "equipment_types": set(),
        "locations": set(),
        "maintenance_types": set(),
        "manufacturers": set(),
        "technicians": set()
    }
    
    # Extract from equipment data
    for equipment in equipment_data:
        entities["equipment_types"].add(equipment.get("equipment_type", "").strip())
        entities["locations"].add(equipment.get("location", "").strip())
        entities["manufacturers"].add(equipment.get("manufacturer", "").strip())
    
    # Extract from maintenance data
    for log in maintenance_logs:
        entities["maintenance_types"].add(log.get("maintenance_type", "").strip())
        entities["technicians"].add(log.get("technician", "").strip())
    
    # Convert to sorted lists, removing empty values
    return {key: sorted([item for item in values if item]) 
            for key, values in entities.items()}

def validate_data_integrity():
    """Perform basic data validation."""
    issues = []
    
    if not equipment_data:
        issues.append("No equipment data loaded")
    if not maintenance_logs:
        issues.append("No maintenance data loaded")
    
    # Check for orphaned maintenance records
    equipment_ids = {eq.get("equipment_id") for eq in equipment_data}
    for log in maintenance_logs:
        if log.get("equipment_id") not in equipment_ids:
            issues.append(f"Maintenance record {log.get('log_id')} references unknown equipment")
    
    return issues

def build_equipment_relationships(equipment_id: str) -> Dict[str, Any]:
    """Build relationships for specific equipment."""
    # Find equipment details
    equipment = next((eq for eq in equipment_data if eq.get("equipment_id") == equipment_id), None)
    if not equipment:
        return None
    
    # Find related maintenance
    related_maintenance = [log for log in maintenance_logs if log.get("equipment_id") == equipment_id]
    
    # Build relationship data
    technicians = list(set(log.get("technician", "") for log in related_maintenance if log.get("technician")))
    maintenance_types = list(set(log.get("maintenance_type", "") for log in related_maintenance if log.get("maintenance_type")))
    total_cost = sum(log.get("cost", 0) for log in related_maintenance)
    
    return {
        "equipment": equipment,
        "maintenance_history": related_maintenance,
        "summary": {
            "maintenance_count": len(related_maintenance),
            "total_cost": total_cost,
            "technicians_involved": technicians,
            "maintenance_types": maintenance_types
        }
    }

def get_equipment_data():
    """Get the current equipment data."""
    return equipment_data

def get_maintenance_logs():
    """Get the current maintenance logs."""
    return maintenance_logs