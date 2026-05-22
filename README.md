# CLI Automation Testing Prototype

This project demonstrates CLI automation testing using Python scripting and Robot Framework.

## Tech Stack
- Python
- Robot Framework
- Git CLI

## Project Structure

cli-automation/
│
├── scripts/
│   └── automation.py
│
└── tests/
    └── cli_test.robot

## Workflow

Robot Framework
↓
Executes Python automation script
↓
Python script runs CLI commands
↓
Robot Framework validates execution
↓
Execution reports generated

## Prerequisites
- Python installed
- Robot Framework installed
- Git installed

## Run Command

```bash
robot tests/cli_test.robot
```