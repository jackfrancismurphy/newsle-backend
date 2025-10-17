# Newsle backend
The backend of Newsle, an API, created with Flask, which calls the news API and edits the data for usage by my frontend.

## Setup
Install api requirements with `python -m pip install -r requirements.txt`
Install testing requirements with `python -m pip install -r requirements-test.txt`

## Running
Run ```python newsle_api.py``` to get the headline normally.

Test commands have the format: \
```python newsle_api.py "<test_headline>"``` \
Example: \
```python newsle_api.py "Earth invaded by Martians"```

## Running Tests

Run: `python -m pytest`

Get a coverage report with: `python -m pytest --cov`
