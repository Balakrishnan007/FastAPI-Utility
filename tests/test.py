"""
Unit tests for the Utility Infrastructure Knowledge Extraction API.

Following the structure provided in the example test file.
Tests both data processing functionality and API endpoints.
"""

import pytest
from fastapi.testclient import TestClient
from main import app
from src.data_processor import extract_entities, equipment_data, maintenance_logs
from src.data_processor import load_equipment_data, load_maintenance_logs

# Add this before the test classes:
#def setup_module():
#    """Load real data before running tests."""
#    load_equipment_data()
#    load_maintenance_logs()

# Create test client for API testing
client = TestClient(app)

class TestDataProcessor:
    """Test class for data processing functionality."""
    
    def test_extract_entities(self):
        """Test entity extraction functionality."""
        # Setup sample data
        global equipment_data, maintenance_logs
        
        # Mock equipment data
        equipment_data = [
            {
                "equipment_id": "TEST001",
                "equipment_type": "Transformer",
                "location": "Test Substation",
                "manufacturer": "TestCorp",
                "status": "Active"
            },
            {
                "equipment_id": "TEST002", 
                "equipment_type": "Generator",
                "location": "Test Plant",
                "manufacturer": "TestGen",
                "status": "Maintenance"
            }
        ]
        
        # Mock maintenance data
        maintenance_logs = [
            {
                "log_id": "LOG001",
                "equipment_id": "TEST001",
                "maintenance_type": "Routine Inspection",
                "technician": "John Doe",
                "status": "Completed"
            },
            {
                "log_id": "LOG002",
                "equipment_id": "TEST002",
                "maintenance_type": "Emergency Repair", 
                "technician": "Jane Smith",
                "status": "In Progress"
            }
        ]
        
        # Test the function
        entities = extract_entities()
        
        # Verify results
        assert "equipment_types" in entities
        assert "locations" in entities
        assert "maintenance_types" in entities
        assert "manufacturers" in entities
        assert "technicians" in entities
        
        # Check specific values
        assert "Transformer" in entities["equipment_types"]
        assert "Generator" in entities["equipment_types"]
        assert "Test Substation" in entities["locations"]
        assert "Routine Inspection" in entities["maintenance_types"]
        assert "John Doe" in entities["technicians"]
        assert "TestCorp" in entities["manufacturers"]
        
        # Verify lists are sorted
        assert entities["equipment_types"] == sorted(entities["equipment_types"])
        assert entities["technicians"] == sorted(entities["technicians"])
    
    def test_extract_entities_empty_data(self):
        """Test extract_entities with empty data."""
        global equipment_data, maintenance_logs
        
        # Setup empty data
        equipment_data = []
        maintenance_logs = []
        
        # Test the function
        entities = extract_entities()
        
        # Verify all lists are empty
        assert entities["equipment_types"] == []
        assert entities["locations"] == []
        assert entities["maintenance_types"] == []
        assert entities["manufacturers"] == []
        assert entities["technicians"] == []


class TestAPI:
    """Test class for API functionality."""
    
    def test_get_equipment_endpoint(self):
        """Test equipment listing endpoint."""
        # Test basic equipment endpoint
        response = client.get("/api/equipment")
        assert response.status_code == 200
        
        data = response.json()
        assert "count" in data
        assert "equipment" in data
        assert isinstance(data["equipment"], list)
    
    def test_get_equipment_with_filter(self):
        """Test equipment endpoint with filters."""
        # Test with equipment type filter
        response = client.get("/api/equipment?equipment_type=Transformer")
        assert response.status_code == 200
        
        data = response.json()
        assert "count" in data
        assert "equipment" in data
        
        # If there are results, they should all be transformers
        for equipment in data["equipment"]:
            assert equipment.get("equipment_type", "").lower() == "transformer"
    
    def test_maintenance_endpoint(self):
        """Test maintenance listing endpoint."""
        response = client.get("/api/maintenance")
        assert response.status_code == 200
        
        data = response.json()
        assert "count" in data
        assert "maintenance" in data
        assert isinstance(data["maintenance"], list)
    
    def test_entities_endpoint(self):
        """Test entities extraction endpoint."""
        response = client.get("/api/entities")
        assert response.status_code == 200
        
        data = response.json()
        assert "entities" in data
        assert "summary" in data
        
        entities = data["entities"]
        assert "equipment_types" in entities
        assert "locations" in entities
        assert "maintenance_types" in entities
        assert "manufacturers" in entities
        assert "technicians" in entities
    
    def test_search_endpoint(self):
        """Test search functionality."""
        # Test search with valid query
        response = client.get("/api/search?query=transformer")
        assert response.status_code == 200
        
        data = response.json()
        assert "query" in data
        assert "total_results" in data
        assert "results" in data
        assert data["query"] == "transformer"
        
        results = data["results"]
        assert "equipment" in results
        assert "maintenance" in results
        assert isinstance(results["equipment"], list)
        assert isinstance(results["maintenance"], list)
    
    def test_search_endpoint_empty_query(self):
        """Test search endpoint with empty query."""
        response = client.get("/api/search?query=")
        assert response.status_code == 400  # Should return bad request
    
    def test_root_endpoint(self):
        """Test root health check endpoint."""
        response = client.get("/")
        assert response.status_code == 200
        
        data = response.json()
        assert "api" in data
        assert "status" in data
        assert "data_summary" in data


# Optional: Run tests directly
if __name__ == "__main__":
    print("Running data processing tests.")
    test_processor = TestDataProcessor()
    test_processor.test_extract_entities()
    test_processor.test_extract_entities_empty_data()
    print("Data processing tests passed!")
    
    print("Running API tests.")
    test_api = TestAPI()
    test_api.test_root_endpoint()
    test_api.test_entities_endpoint()
    print(" API tests passed!")
    
    print("All tests completed successfully!")