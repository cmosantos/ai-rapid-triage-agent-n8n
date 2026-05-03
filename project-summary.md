# Project Summary

## Project Name

AI Rapid Triage Agent

## Description

AI Rapid Triage Agent is a practical automation project designed to assist IT support teams with the initial triage of support requests.

The workflow receives a support request through an n8n chat interface, sends the request to an AI Agent, extracts structured information from the response, records the ticket in Google Sheets, and sends a formatted email summary to the analyst through Gmail.

## Problem Solved

In many IT support environments, analysts spend time reading support messages, identifying the category, defining priority, checking whether the issue may involve security risk, and deciding which team should handle the request.

This workflow automates the first triage step and helps create a more consistent support process.

## What the Agent Does

The AI Agent analyzes the incoming request and generates:

- Ticket title
- Summary
- Category
- Priority
- Security risk
- Business impact
- Recommended actions
- Suggested response to the user
- Internal technical note
- Human review flag

The JavaScript Code node then enriches the result with:

- Timestamp
- Ticket ID
- SLA target
- Assigned queue
- Escalation requirement
- Ticket status

## Workflow Steps

1. The user sends a support request in the n8n chat.
2. The AI Agent analyzes the message.
3. The Code node cleans and structures the output.
4. Google Sheets receives a new row with the ticket data.
5. Gmail sends a formatted summary email.
6. The chat returns a confirmation and the triage result.

## Example Categories

- Microsoft 365
- Exchange Online
- Microsoft Teams
- Entra ID / Azure AD
- Password / MFA
- Network / VPN
- AWS / IAM
- Security / Phishing
- Access Request
- Software / Application
- Device / Hardware
- Other

## Portfolio Value

This project demonstrates applied knowledge in AI automation, IT support operations, workflow orchestration, data logging, and email notification using n8n.
