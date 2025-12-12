# Bitasmbl-Weather-Dashboard-a8f2ee-b9bbb1a779c7

## Description
Build a web application that displays current weather, multi-day forecasts, and visualizes trends with charts. The project focuses on integrating APIs, dynamic front-end updates, and data visualization for an interactive user experience.

## Tech Stack
- Java
- FastAPI
- React

## Requirements
- Fetch real-time weather data from a public API
- Display multi-day weather forecasts with clear UI elements
- Visualize temperature, humidity, or other metrics with charts
- Support user interactions, such as searching by city
- Optionally cache API responses to improve performance

## Installation
bash
git clone https://github.com/MrBitasmblTester/Bitasmbl-Weather-Dashboard-a8f2ee-b9bbb1a779c7.git
cd Bitasmbl-Weather-Dashboard-a8f2ee-b9bbb1a779c7


### Backend (FastAPI)
bash
pip install fastapi uvicorn


### Frontend (React)
bash
cd frontend
npm install


## Usage
### Backend
bash
uvicorn main:app --reload


### Frontend
bash
cd frontend
npm start


## Implementation Steps
1. Set up React app layout for current weather, forecast, and charts.
2. Configure FastAPI routes to proxy requests to a public weather API.
3. Implement Java components or services as needed within the backend layer.
4. Fetch real-time weather data from FastAPI in React and display current conditions.
5. Add multi-day forecast UI elements and bind them to API data.
6. Integrate chart components to visualize temperature, humidity, or other metrics.
7. Implement city search input and connect it to API queries.
8. Optionally add response caching in the backend to improve performance.

## API Endpoints
- `GET /weather/current?city={city}`
- `GET /weather/forecast?city={city}`