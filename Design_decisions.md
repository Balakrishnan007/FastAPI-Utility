# Design Decisions

## Utility Infrastructure Knowledge Extraction API

### Technology Choices
- **FastAPI** over Flask - automatic documentation, built-in validation, async support
- **In-memory storage** with global variables - meets requirements, simple for demo
- **Startup data loading** - better UX than manual POST endpoint

### Architecture
- **Modular structure**: main.py (setup) + src/data_processor.py (data logic) + src/api.py (endpoints)
- **5 endpoints** - exceeds minimum of 3, covers all functionality
- **Integrated approach** - combined location data with equipment instead of separate endpoint

### Data Processing
- **Sets for entity extraction** - automatic deduplication, O(1) performance
- **Simple text search** - sufficient for project scope, easy to maintain
- **Comprehensive error handling** - proper HTTP status codes (400, 404, 503, 500)

### Testing Strategy
- **Integration-focused testing** - validates entire pipeline works
- **FastAPI TestClient** - proper API testing approach
- **Real data emphasis** - ensures compatibility with actual files

### Development Approach
- **Working solution first** - ensure deliverable, then refactor
- **Incremental building** - core features → enhancements → organization
- **Time-boxed scope** - prioritized must-haves over nice-to-haves

### Key Trade-offs
- Chose simplicity over advanced features (basic search vs Elasticsearch)
- Prioritized functionality over perfect test coverage
- Selected demo-appropriate solutions over production-scale architecture