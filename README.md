### Test Automation Project for [DemoQA.com](https://demoqa.com/)

[![Website](https://img.shields.io/website.svg?url=https://prog420.github.io/demo-qa)]()
[![Python](https://img.shields.io/badge/python-3.10-blue)]()

---

Latest Test Report: [Github Page](https://prog420.github.io/demo-qa)

---

**Test Reports:** [Allure](https://allurereport.org/)

**CI:** [Github Actions](https://github.com/features/actions/)

---

### &nbsp;&nbsp;🛠️ Prerequisites

[![Pytest](https://img.shields.io/badge/pytest-8.3.2-blue)](https://pypi.python.org/pypi/pytest)
[![pytest-xdist](https://img.shields.io/badge/pytest--xdist-3.6.1-blue)](https://pypi.org/project/pytest-xdist/)
[![Selenium](https://img.shields.io/badge/selenium-4.23.1-blue)](https://pypi.org/project/selenium/)
[![Allure Pytest](https://img.shields.io/badge/allure--pytest-2.13.5-blue)](https://pypi.python.org/pypi/allure-pytest)

---

### &nbsp;&nbsp;🛠️ Running Tests

#### a) Github Actions CI

Launch New Test Run:

1. Navigate to `Actions` tab.
2. Select `Allure Report CI`.
3. Click `Run Workflow`.
4. Select `Use Workflow From:`: `Branch: main`.
5. Click `Run Workflow`.
6. Wait until the job is complete.
7. Navigate to [Allure Report Page](https://prog420.github.io/demo-qa).

#### b) Local Machine:

1. Clone repository, install dependencies:

```bash
# Clone repository
git clone ...

# Install virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

2. Start new test run:

```bash
pytest -vs --alluredir=allure-reports
```

3. Check allure report:

```bash
allure serve allure-reports
```

---

### &nbsp;&nbsp;🛠️ Custom CLI Arguments:

1. `--headless` - run tests without loading the browser's UI.
2. `--ignore-passed-test-attachments` - do not attach screenshots / logs to the Allure report.