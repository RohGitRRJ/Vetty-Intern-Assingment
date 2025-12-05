VETTY CRYPTO MARKET API

A lightweight, production-ready FastAPI service that pulls real-time cryptocurrency market data from CoinGecko and exposes it via secure JWT-based APIs. Prices are provided in INR and CAD. This project is designed as a clean, minimal, and testable backend service.

------------------------------------------------------------

KEY CAPABILITIES

- Real-time cryptocurrency prices
- Supports INR and CAD conversions
- Filter coins by:
  - Coin IDs
  - Market categories
- Secured APIs using JWT authentication
- Standard utility endpoints:
  - /health for service status
  - /version for app metadata
- Built-in interactive API docs at /docs
- Automated tests using pytest
- Docker support for containerized deployment

------------------------------------------------------------

GETTING STARTED

1. Set up a virtual environment

Command:
python3 -m venv venv
source venv/bin/activate
(For Windows: venv\Scripts\activate)

2. Install required packages

Command:
pip install -r requirements.txt

3. Start the API server

Command:
uvicorn app.main:app --reload

Once the server is running, open the following URL in your browser:
http://127.0.0.1:8000/docs

------------------------------------------------------------

AUTHENTICATION (DEMO SETUP)

To access protected endpoints:

1. Send a POST request to:
/auth/token

With the following form values:
username = demo
password = demo

2. The API will return a JWT token.

3. Use this token in the request header for all secured APIs:

Authorization: Bearer <your_token_here>

------------------------------------------------------------

CORE API ROUTES

1. GET /coins?page_num=1&per_page=10
Returns a paginated list of available coins with:
- ID
- Symbol
- Name

2. GET /coins/markets?ids=bitcoin,ethereum
Fetches live market prices in INR and CAD for the specified coins.

3. GET /categories
Lists all CoinGecko categories.

4. GET /health
Confirms service availability.

5. GET /version
Displays application name and current version.

------------------------------------------------------------

RUNNING TESTS

To execute all unit tests, run:
pytest

Test coverage includes:
- JWT authentication flow
- Health and version endpoints
- A protected API route
- External CoinGecko calls are mocked using monkeypatch

------------------------------------------------------------

DOCKER USAGE

To build the Docker image:

docker build -t vetty-crypto-api .

To run the container:

docker run --rm -p 8000:8000 vetty-crypto-api

------------------------------------------------------------

IMPORTANT NOTES

- Update the JWT secret key and demo credentials in the .env file before using this in production.
- This API does not store market data. All information is fetched live from CoinGecko.
- Be mindful of CoinGecko public API rate limits during deployment.

------------------------------------------------------------

This project demonstrates secure API design, third-party data integration, automated testing, and containerized deployment using FastAPI.
