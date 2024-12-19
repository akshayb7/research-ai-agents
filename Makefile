# Makefile

# Default target
.PHONY: run

# Target to run the script with an argument
run:
	@if [ -z "$(topic)" ]; then \
		echo "Error: Argument 'topic' is required. Use 'make run topic=<your_argument>'."; \
		exit 1; \
	fi
	python src/research_crew/main.py $(topic)