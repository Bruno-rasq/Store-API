.PHONY: test

install:
	@pip install -r requiriments.txt

run:
	@uvicorn store.main:app --host 0.0.0.0 --port 8080 --reload

test:
	@pytest -v tests