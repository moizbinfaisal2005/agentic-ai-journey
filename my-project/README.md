# Customer Feedback Analyzer

A small AI-powered application that analyzes customer reviews, classifies them as positive/negative/neutral, assigns a sentiment score from 1 to 5, and identifies the main product/theme issue or strength such as delivery, taste, price, service, or quality.

## Overview

This project has two main parts:

- A FastAPI backend in `api.py` that sends each customer review to Google Gemini and returns structured JSON.
- A Streamlit frontend in `app.py` that lets users paste reviews, run analysis, view results, and save them to a SQLite database.

The app also stores saved review history in `feedback.db` so users can revisit past analyses.

## Project structure

- `app.py` – Streamlit UI for uploading/pasting reviews and displaying results
- `api.py` – FastAPI backend for AI sentiment analysis
- `database.py` – SQLite helper functions for saving and loading feedback history
- `sample_reviews.txt` – Example review input data
- `requirements.txt` – Python dependencies
- `feedback.db` – Local SQLite database generated at runtime

## Features

- Paste one review per line or analyze multiple reviews at once
- Sentiment classification:
  - positive
  - negative
  - neutral
- Score range from 1 to 5
- Theme detection from a fixed set:
  - delivery
  - taste
  - price
  - service
  - quality
- Batch summary metrics in the Streamlit dashboard
- Save analyzed reviews into SQLite
- View past saved history from the database

## Tech stack

- Python
- FastAPI
- Streamlit
- SQLite
- Google Gemini API
- Python-dotenv

## Setup

1. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your Google API key:

   ```env
   GOOGLE_API_KEY=your_api_key_here
   ```

4. Start the backend API:

   ```bash
   uvicorn api:app --reload
   ```

5. In a second terminal, start the Streamlit app:

   ```bash
   streamlit run app.py
   ```

6. Open the local Streamlit URL in your browser and begin analyzing reviews.

## Example input

You can paste reviews like this into the web app:

```text
The delivery was very fast and the product was excellent.
The taste was bland and the service was slow.
Affordable pricing and good quality overall.
```

## How the app works

1. The user enters customer feedback in the Streamlit UI.
2. Each review is sent to the FastAPI backend.
3. The AI model returns JSON with:
   - `label`
   - `score`
   - `theme`
4. Results are displayed in a table and summarized in metrics.
5. The user can save the reports to SQLite for later review.

## Notes

- The backend expects a valid `GOOGLE_API_KEY` in the environment.
- The app uses a local SQLite database file called `feedback.db`.
- The database is created automatically when the app starts.

## License

This project is intended for educational and demo use.
