*** Settings ***
Library    OperatingSystem

*** Variables ***
${LOG_DIR}    logs

*** Test Cases ***
Validate Latest Hotfix Log

    ${files}=    List Files In Directory    ${LOG_DIR}

    ${latest}=    Set Variable    ${files}[-1]

    ${content}=    Get File    ${LOG_DIR}/${latest}

    Should Contain    ${content}    HOTFIX_CREATED
    Should Contain    ${content}    CODE_COMMITTED
    Should Contain    ${content}    PR_OPENED
    Should Contain    ${content}    PR_MERGED
    Should Contain    ${content}    RELEASE_CREATED