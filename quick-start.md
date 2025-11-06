# Практический стартовый шаблон (Quick Start)

## Для студентов: Как начать проект с правильной структурой

### Шаг 1: Создайте репозиторий с нужной структурой

```bash
git clone <your-repo-url>
cd your-project
```

### Шаг 2: Создайте структуру папок

```bash
mkdir -p src tests data scripts docs .github/workflows
touch .gitignore requirements.txt README.md
touch src/__init__.py
touch tests/__init__.py
```

### Шаг 3: Заполните `.gitignore`

```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Virtual environments
venv/
env/
ENV/

# Environment variables
.env
.env.local

# IDE
.vscode/
.idea/
*.swp
*.swo

# Data files (если большие)
data/*.csv
data/*.xlsx
!data/sample.csv

# Generated files
*.log
.DS_Store
```

### Шаг 4: Создайте `requirements.txt`

```
# Core dependencies
numpy>=1.20.0
pandas>=1.3.0
scikit-learn>=1.0.0

# Testing
pytest>=7.0.0
pytest-cov>=3.0.0

# Code quality
flake8>=4.0.0
black>=22.0.0

# Visualization (optional)
matplotlib>=3.4.0
plotly>=5.0.0
```

### Шаг 5: Создайте базовый `README.md`

```markdown
# Project Name

## Description
[Brief description of what this project does]

## Installation

### Prerequisites
- Python 3.8+
- pip or conda

### Setup
```bash
git clone <repo-url>
cd <project-name>
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

### Basic Example
```python
from src.main import analyze_data

result = analyze_data("data/sample.csv")
print(result)
```

### Advanced Usage
[Add more complex examples]

## Project Structure
```
.
├── src/                 # Source code
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
├── tests/              # Unit tests
│   ├── __init__.py
│   └── test_main.py
├── data/               # Data files
│   └── sample.csv
├── docs/               # Documentation
├── scripts/            # Utility scripts
├── .github/workflows/  # CI/CD
├── README.md
├── requirements.txt
└── .gitignore
```

## Requirements
- NumPy >= 1.20.0
- Pandas >= 1.3.0
- Scikit-learn >= 1.0.0

## Testing

Run tests with:
```bash
pytest
```

Run with coverage:
```bash
pytest --cov=src tests/
```

## Contributing
[Contribution guidelines]

## License
[License info]

## Author
[Your name]
```

### Шаг 6: Создайте GitHub Actions workflow

Создайте файл `.github/workflows/tests.yml`:

```yaml
name: Tests and Code Quality

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.8', '3.9', '3.10']

    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Lint with flake8
      run: |
        flake8 src tests --count --select=E9,F63,F7,F82 --show-source --statistics
        flake8 src tests --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    
    - name: Format check with black
      run: black --check src tests || true
    
    - name: Run tests
      run: pytest tests/ -v --cov=src --cov-report=xml
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        files: ./coverage.xml
```

### Шаг 7: Создайте первый коммит

```bash
git add .
git commit -m "Initial project setup with structure and CI/CD"
git push
```

---

## Чек-лист для студента перед сдачей

### ✓ Полезность задачи (4 балла)
- [ ] Проект решает реальную проблему в выбранной области
- [ ] Область применения четко определена в README
- [ ] Демонстрирует понимание проблемы
- [ ] Связан с ИИ в образовании, обработкой данных или смежными областями

### ✓ Оформление репозитория (3 балла)
- [ ] `.gitignore` присутствует и заполнен
- [ ] `requirements.txt` содержит все зависимости
- [ ] Структура папок логична (src/, tests/, data/, docs/)
- [ ] Код и конфиги разделены по папкам
- [ ] Нет нежелательных файлов в репо (`.pyc`, `__pycache__`, `.env`)
- [ ] Проверено: `git status` не показывает нежелательные файлы

### ✓ Работоспособность + CI/CD (4 балла)
- [ ] Код работает без ошибок (тестировано локально)
- [ ] GitHub Actions workflow настроен в `.github/workflows/`
- [ ] Workflow запускается на push и pull_request
- [ ] Проверка PEP 8 включена (flake8 или black)
- [ ] Unit tests писать (как минимум 3-5 простых тестов)
- [ ] Тесты запускаются в workflow
- [ ] Последний push имеет статус "success" в Actions
- [ ] Badge статуса добавлен в README

### ✓ Качество документации (2 балла)
- [ ] README содержит описание проекта (What, Why)
- [ ] Есть инструкции по установке
- [ ] Есть примеры использования с кодом
- [ ] Есть примеры выводов/результатов
- [ ] Описана структура проекта
- [ ] Указаны требования (Python version, dependencies)
- [ ] Нет опечаток, текст ясный

### ✓ Креативное использование CI/CD (2 баллов)
- [ ] CI/CD делает что-то большее, чем просто проверку кода
- [ ] Используется одна из продвинутых техник:
  - [ ] Scheduled workflow (cron schedule)
  - [ ] Workflow dispatch (manual trigger)
  - [ ] Artifact upload
  - [ ] Data generation/update с автокоммитом
  - [ ] Deploy (GitHub Pages, etc.)
  - [ ] Уведомления (Slack, email)
- [ ] Это имеет практическую ценность для проекта
- [ ] Dokumentировано в README

### Финальные проверки
- [ ] Всё закоммичено и запушено на `main` (или указанную ветку)
- [ ] GitHub Actions последний run имеет статус ✅ success
- [ ] Проект доступен на https://github.com/[username]/[project]
- [ ] README открывается и читается нормально
- [ ] Ссылка на проект готова к передаче

---

## Типичные проблемы и их решение

### Проблема: GitHub Actions fails с ошибкой "ModuleNotFoundError"

**Решение:**
```bash
# 1. Убедитесь, что все зависимости в requirements.txt
pip freeze > requirements.txt

# 2. Проверьте, что в workflow установлены зависимости:
- name: Install dependencies
  run: |
    pip install -r requirements.txt
```

### Проблема: Файлы в .gitignore не игнорируются

**Решение:**
```bash
# Удалить уже отслеживаемые файлы
git rm --cached __pycache__ -r
git rm --cached *.pyc
git commit -m "Remove cached files"
git push
```

### Проблема: CI/CD не запускается

**Решение:**
1. Проверьте `.github/workflows/` папка существует
2. Проверьте имя workflow файла (должен оканчиваться на `.yml` или `.yaml`)
3. Проверьте trigger (`on: push`, `on: [push, pull_request]`)
4. Смотрите логи в Actions tab на GitHub

### Проблема: Black/flake8 не работает в workflow

**Решение:**
```bash
# Добавьте в requirements.txt
flake8>=4.0.0
black>=22.0.0

# В workflow используйте:
- name: Run tests
  run: |
    flake8 src --count --select=E9,F63,F7,F82 --show-source --statistics || true
    pytest tests/ -v
```

### Проблема: README не отображается правильно

**Решение:**
- Используйте только `.md` (Markdown) формат
- Проверьте синтаксис на https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
- Code blocks оформляйте с тройными backticks: ` ``` `

---

## Примеры креативных workflows

### Пример 1: Scheduled Analysis

```yaml
name: Daily Analysis

on:
  schedule:
    - cron: '0 2 * * *'  # Ежедневно в 2 ночи UTC

jobs:
  analyze:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      
      - name: Install dependencies
        run: pip install -r requirements.txt
      
      - name: Run analysis
        run: python scripts/daily_analysis.py
      
      - name: Commit results
        run: |
          git config user.name "Analysis Bot"
          git config user.email "bot@example.com"
          git add reports/
          git commit -m "Daily analysis: $(date)" || true
          git push
```

### Пример 2: Manual Trigger (Workflow Dispatch)

```yaml
name: Generate Report

on:
  workflow_dispatch:
    inputs:
      date_range:
        description: 'Date range for analysis'
        required: true
        default: '30'

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      
      - name: Install dependencies
        run: pip install -r requirements.txt
      
      - name: Generate report
        run: python scripts/generate_report.py --days ${{ github.event.inputs.date_range }}
      
      - name: Upload artifact
        uses: actions/upload-artifact@v3
        with:
          name: report-$(date +%Y-%m-%d)
          path: reports/
          retention-days: 30
```

### Пример 3: Artifact Upload

```yaml
name: Build and Upload

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      
      - name: Install and run
        run: |
          pip install -r requirements.txt
          python main.py > output.txt
      
      - name: Upload output
        uses: actions/upload-artifact@v3
        with:
          name: program-output
          path: output.txt
```

---

## Рекомендованные инструменты и библиотеки

### Data Analysis
- `pandas` — работа с табличными данными
- `numpy` — численные вычисления
- `scipy` — научные вычисления

### Machine Learning
- `scikit-learn` — классический ML
- `xgboost`, `lightgbm` — gradient boosting
- `transformers` — NLP с трансформерами

### Visualization
- `matplotlib` — базовые графики
- `seaborn` — красивые статистические графики
- `plotly` — интерактивные графики

### Testing
- `pytest` — фреймворк для тестов
- `pytest-cov` — покрытие кода

### Code Quality
- `flake8` — проверка стиля
- `black` — форматирование кода
- `pylint` — статический анализ

### Text Processing
- `nltk` — обработка текста
- `spacy` — NLP
- `textblob` — простая обработка текста

