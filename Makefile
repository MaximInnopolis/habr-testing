# Variables definition
PYTHON = python3
PIP = pip3
SPACY_MODEL = ru_core_news_sm

.DEFAULT_GOAL := help

help:
	@echo "Available commands:"
	@echo "  make install    - Установить зависимости"
	@echo "  make spacy      - Скачать модель spaCy"
	@echo "  make test       - Запустить тесты"

# Dependencies setup
install:
	$(PIP) install -r requirements.txt

# Spacy model download
spacy:
	$(PYTHON) -m spacy download $(SPACY_MODEL)

# Tests run
test:
	$(PYTHON) -m pytest -s

