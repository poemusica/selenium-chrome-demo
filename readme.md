# Selenium Tests using Headless Chrome

Follow these instructions to run the demo:

Step 1. Create and activate a virtual environment.

`virtualenv env` (or `virtualenv env --always-copy` for Windows users)

`source bin/env/activate`

Step 2. Install the requirements.

`pip3 install -r requirements.txt`

Step 3. [Install Chrome and ChromeDriver](https://docs.google.com/document/d/1NYAjxA0tvqaxoTSptKO0dAfP8ZmvfpRRMdfFFK0dATw/).


Step 4. In one terminal, start the server.

`python3 server.py`

Step 5. In another terminal, run the tests.

`python3 tests-simple.py` or `python3 tests.py`
