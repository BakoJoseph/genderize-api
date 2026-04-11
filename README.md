# Genderize API

A Flask-based REST API that integrates with the Genderize.io service to predict the gender of a given name.

## 🚀 Live URL

*(To be deployed)*

## 📌 API Endpoint

### GET /api/classify

Predicts the gender of a name using the Genderize API.

**Query Parameters:**

- `name` (string, required): The name to classify

**Example Request:**

```
GET /api/classify?name=John
```

**Success Response (200):**
```json
"status": "success",
"data": {
    "gender": "male",
    "is_confident": true,
    "name": "john",
    "probability": 1.0,
    "processed_time": "2026-04-11T10:57:00.632189Z",
    "sample_size": 2692560,
    "status": "success"
}
```

**Error Responses:**
- **400 Bad Request:** Missing or empty name parameter
```json
{
  "status": "error",
  "message": "Missing or empty name parameter"
}
```

- **422 Unprocessable Entity:** name is not a string 
```json
{
  "status": "error",
  "message": "Name parameter must be a string"
}
```

- **502 Bad Gateway:** Upstream API failure
```json
{
  "status": "error",
  "message": "Upstream or server failure"
}
```

## Features

- **External API Integration:** Seamlessly connects to Genderize.io
- **Confidence Calculation:** Determines confidence based on probability (>=0.7) and sample count (>=100)
- **Comprehensive Error Handling:** Handles various edge cases and API failures
- **CORS Enabled:** Supports cross-origin requests
- **Input Validation:** Ensures name is a non-empty string

## Prerequisites

- Python 3.7+
- Virtual environment (recommended)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd genderize-api
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv .venv
   # On Windows:
   .\.venv\Scripts\Activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running Locally

1. Activate the virtual environment (if not already):
   ```bash
   # Windows:
   .\.venv\Scripts\Activate
   # macOS/Linux:
   source .venv/bin/activate
   ```

2. Run the application:
   ```bash
   python app.py
   ```

The API will be available at `http://localhost:5000`

## Dependencies

- Flask: Web framework
- requests: HTTP library for API calls
- python-dotenv: Environment variable management

## Project Structure

```
genderize-api/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── tests/             # Test files
└── utils/             # Utility modules
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
