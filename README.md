# Stevesie Python Client

**This library is under development, please be careful and report any bugs you find! <3**

## Installation

This package will be available on PyPi when it's a little more mature, but until then you'll need to download (yes, actually download or clone this repo) and make the `./stevesie` folder available to your Python code.

For example, if I want to run the file `main.py`, I would need to make sure the `stevesie` folder is in the same directory as `main.py`, and then we can perform imports like this in `main.py`: `from stevesie.worker import Worker`

## Usage

This code is currently meant to help you interact with your workers programmatically, either downloading collection results the worker has already gathered in JSON format, or to run workers with special parameters.

```py
from stevesie.worker import Worker

# find your ID from https://stevesie.com/workers/WORKER_ID and insert
worker = Worker(WORKER_ID)

# fetch metadata about the worker, like its task or workflow definition
worker.fetch()

# see what parameters are available to run with
print(worker.run_params())

# download all the workers collection results in-memory
worker_results = worker.fetch_results()

# save the results as JSON locally
worker_results.save_to_file(CACHE_FILE_LOCATION)

# re-load the local JSON back into memory
worker.load_results(CACHE_FILE_LOCATION)

# show the worker extraction results
print(worker_results.items())

# run the worker with custom parameters
worker.run({'PARAM_ID': 'custom_value_from_python'})
```

## Sample Projects

If you build something cool, let us know and we'll link to it here: