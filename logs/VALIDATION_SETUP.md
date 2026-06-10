# Agent/Log Validation Demo - Setup Instructions

## Prerequisites

### 1. Python

Install Python 3.10+ and verify installation:

```bash
python --version
```

### 2. Robot Framework

Install Robot Framework:

```bash
pip install robotframework
```

Verify installation:

```bash
robot --version
```

---

## Project Structure

```text
project/
│
├── logs/
│
└── tests/
    └── hotfix_log_validation.robot
```

---

## Execute Validation

Run from the project root directory:

```bash
robot tests/hotfix_log_validation.robot
```

---

## Generated Outputs

Robot Framework generates the following output files:

* report.html
* log.html
* output.xml

These files contain execution results, validation details, and test reports.

---

## Validation Scope

The log validation workflow verifies:

* Presence of expected workflow events
* Correct execution flow
* Required activity entries
* Absence of error conditions
* Overall workflow completion status

---

## Objective

Evaluate Robot Framework's capability to analyze and validate workflow/execution logs and generate automated PASS/FAIL results based on predefined validation rules.
