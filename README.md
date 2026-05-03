# AI Rapid Triage Agent

AI Rapid Triage Agent is an automation workflow built with n8n to support IT helpdesk operations.

The workflow receives a support request through a chat interface, analyzes the issue with an AI Agent, classifies the ticket, defines priority, evaluates security risk, suggests technical actions, registers the ticket in Google Sheets, and sends a formatted email summary through Gmail.

## Project Objective

The goal of this project is to demonstrate how AI agents and automation workflows can improve IT support triage by reducing manual work, standardizing ticket classification, and helping analysts respond faster to common technical requests.

This project was created as a practical AI automation portfolio project focused on real-world IT support scenarios.

## Main Features

- Receives support requests through an n8n chat interface
- Uses an AI Agent to classify and summarize the issue
- Identifies category, priority, security risk, business impact, and human review requirement
- Generates recommended technical actions for the support analyst
- Generates a suggested response to the end user
- Creates a ticket ID automatically
- Defines SLA target based on priority
- Assigns the ticket to a support queue
- Registers the ticket in Google Sheets
- Sends a formatted email summary through Gmail

## Technologies Used

- n8n
- OpenAI Chat Model
- JavaScript Code Node
- Google Sheets
- Gmail
- AI Agent workflow orchestration

## Example Use Case

Input example:

User reports that they cannot access the corporate email. The account appears to be blocked and the MFA code is not being received.

Expected output example:

Ticket Title: Corporate email access blocked  
Category: Microsoft 365  
Priority: High  
Security Risk: Medium  
SLA: 4 hours  
Assigned Queue: Microsoft 365 Support  
Needs Human Review: Yes  

## Workflow Architecture

Chat Trigger  
AI Agent  
Code in JavaScript  
Google Sheets  
Gmail  
Chat Response  

## Business Value

This workflow shows how AI can support IT operations by creating faster, more consistent, and more structured triage processes.

Instead of manually reading each request and deciding how to classify it, the AI Agent provides a first analysis that can be reviewed and improved by a human analyst.

## Repository Structure

ai-rapid-triage-agent-n8n/  
README.md  
project-summary.md  
workflow-overview.md  
setup-guide.md  
screenshots/  
workflow/ai-rapid-triage-agent.json  

## Status

Version 1 completed as a functional MVP.

## Next Improvements

- Add conditional email alerts only for High or Critical tickets
- Add approval workflow for access requests
- Add integration with Microsoft Teams or Slack
- Add dashboard for ticket metrics
- Add knowledge base integration with Dify or Langflow
- Add real helpdesk integration such as Jira, ServiceNow, Zendesk, or Freshservice
