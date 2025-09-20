# GitHub Actions Flask API Demo

This is a simple Flask REST API application designed for demonstrating GitHub Actions CI/CD workflows. The application provides three endpoints and serves as a learning resource for GitHub Actions integration.

**Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.**

## Working Effectively

### Bootstrap and Setup
- Install Python dependencies:
  - `pip3 install flask` -- installs Flask and dependencies, takes ~30 seconds
  - `pip3 install flake8 pytest` -- installs development tools, takes ~30 seconds

### Build and Run
- **CRITICAL**: No traditional "build" step required - this is a Python script
- Run the Flask application:
  - `python3 app.py` -- starts development server on http://0.0.0.0:5001, takes ~2 seconds to start
  - Server runs in debug mode with auto-reload enabled
  - Press Ctrl+C to stop the server

### Testing and Validation
- **MANUAL VALIDATION REQUIREMENT**: Always test all three endpoints after making changes:
  - Root endpoint: `curl http://localhost:5001/` -- should return JSON with "Hello! Flask API is running 🚀" message
  - Health check: `curl http://localhost:5001/health` -- should return JSON with "status": "ok"  
  - Echo endpoint: `curl -X POST -H "Content-Type: application/json" -d '{"test": "message"}' http://localhost:5001/echo` -- should return JSON with "received": {"test": "message"}
  - **All endpoints must respond with 200 status codes and proper JSON**

### Code Quality
- Run linting: `flake8 app.py` -- checks PEP 8 compliance, takes <1 second
- Run Python syntax check: `python3 -m py_compile app.py` -- validates syntax, takes <1 second
- **CRITICAL**: Fix all flake8 issues before committing - the application currently has style violations that should be addressed

### Testing Framework  
- Create test files using pytest framework
- Run tests: `python3 -m pytest [test_file.py] -v` -- takes <1 second for typical test suite
- Tests should validate all three endpoints using Flask's test client
- Always test both successful requests and error conditions

## GitHub Actions Integration
- Workflow file: `.github/workflows/ci-demo.yml`
- **Current workflow is basic** - only echoes build and test messages
- Triggered on push to `master` branch  
- Runs on `ubuntu-latest`
- **No actual build or test execution currently configured**

## Repository Structure
```
├── .github/
│   └── workflows/
│       └── ci-demo.yml     # Basic GitHub Actions workflow
├── app.py                  # Main Flask application
├── text.txt               # Developer notes/changelog
└── .gitignore             # Python-specific ignore patterns
```

## Critical Implementation Details
- **Port Configuration**: Application runs on port 5001 (not standard 5000)
- **Debug Mode**: Always runs in debug mode with auto-reload
- **Host Binding**: Binds to all interfaces (0.0.0.0) for container compatibility
- **No Database**: Application is stateless - no database setup required
- **No Authentication**: All endpoints are public - no authentication required

## Timing Expectations
- **pip install flask**: ~30 seconds - NEVER CANCEL, set timeout to 60+ seconds
- **pip install development tools**: ~30 seconds - NEVER CANCEL, set timeout to 60+ seconds  
- **Application startup**: ~2 seconds
- **Endpoint response time**: <100ms for all endpoints
- **Linting with flake8**: <1 second
- **Running pytest**: <1 second for basic test suite
- **NEVER CANCEL any pip install commands** - they may appear to hang but will complete

## Validation Scenarios
After making any changes to `app.py`, **ALWAYS** execute this complete validation sequence:

1. **Syntax Check**: `python3 -m py_compile app.py`
2. **Style Check**: `flake8 app.py` 
3. **Start Application**: `python3 app.py` (let it start completely)
4. **Test Root Endpoint**: `curl http://localhost:5001/` - verify "Hello! Flask API is running 🚀" response
5. **Test Health Endpoint**: `curl http://localhost:5001/health` - verify {"status": "ok"} response  
6. **Test Echo Endpoint**: `curl -X POST -H "Content-Type: application/json" -d '{"test": "validation"}' http://localhost:5001/echo` - verify echo response
7. **Stop Application**: Ctrl+C
8. **Run Tests**: `python3 -m pytest [test_file] -v` if tests exist

**Do not commit changes until ALL validation steps pass successfully.**

## Common Tasks

### Adding New Endpoints
- Add route function to `app.py`
- Follow existing pattern: `@app.route("/path", methods=["GET"])` 
- Always return JSON using `jsonify()`
- **Always test manually with curl after adding**

### Updating GitHub Actions
- Edit `.github/workflows/ci-demo.yml` 
- Current workflow only echoes messages - enhance as needed
- Test workflow by pushing to `master` branch

### Troubleshooting
- **"Module not found" errors**: Run `pip3 install flask`
- **Port already in use**: Kill existing Python processes or use different port
- **Import errors**: Check Python path and ensure `app.py` is in working directory
- **JSON parsing errors**: Ensure Content-Type header is set correctly for POST requests

## Dependencies Summary
**Required packages:**
- `flask` - Web framework (automatically installs: blinker, itsdangerous, werkzeug)

**Development packages:**  
- `flake8` - Code linting
- `pytest` - Testing framework

**No requirements.txt file exists** - install packages manually with pip3 commands above.