*** Settings ***
Library    OperatingSystem

*** Variables ***
${LOG_FILE}    logs/hotfix_001.log

*** Test Cases ***
Validate Hotfix Workflow

    File Should Exist    ${LOG_FILE}

    ${content}=    Get File    ${LOG_FILE}

    Should Contain    ${content}    HOTFIX_CREATED
    Should Contain    ${content}    CODE_COMMITTED
    Should Contain    ${content}    PR_OPENED
    Should Contain    ${content}    PR_MERGED
    Should Contain    ${content}    RELEASE_CREATED

    Should Not Contain    ${content}    ERROR