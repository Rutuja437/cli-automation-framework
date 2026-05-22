*** Settings ***
Library    Process

*** Test Cases ***
Run CLI Automation
    ${result}=    Run Process
    ...    python scripts/automation.py
    ...    shell=True

    Log    ${result.stdout}
    Log    ${result.stderr}

    Should Be Equal As Integers
    ...    ${result.rc}
    ...    0