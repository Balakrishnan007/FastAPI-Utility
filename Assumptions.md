# Key Assumptions Made

## Data Assumptions
- **File format** - CSV and JSON follow provided sample structure exactly
- **Data size** - Small to medium datasets that fit in memory (< 100MB)
- **Data relationships** - equipment_id connects CSV and JSON data (foreign key)
- **Data quality** - Files are valid, UTF-8 encoded, no corruption

## Technical Assumptions  
- **Environment** - Development/demo context, not production scale
- **Security** - No authentication required, trusted network usage
- **Performance** - Sub-second response times acceptable
- **Concurrency** - Single-server, read-heavy workload

## Business Assumptions
- **Entity extraction** - Case-insensitive, whitespace trimmed, sorted output
- **Search** - Simple substring matching sufficient
- **API usage** - Standard HTTP GET requests, JSON responses

## Scope Assumptions
- **Time constraint** - 4-hour window prioritizes core functionality
- **Demo purpose** - Working solution over perfect implementation
- **Future scaling** - Database integration would be next step for production