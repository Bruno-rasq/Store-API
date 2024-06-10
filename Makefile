run:
	@uvicorn store.main:app --host 0.0.0.0 --port 8080 --reload


.PHONY: test

test:
	pytest