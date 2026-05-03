# Setup Guide

## Requirements

To reproduce this project, you need:

- n8n account or self-hosted n8n instance
- OpenAI credentials configured in n8n
- Google Sheets connection configured in n8n
- Gmail connection configured in n8n
- A Google Sheets spreadsheet to store ticket records

## Google Sheets Setup

Create a spreadsheet named:

AI Rapid Triage Tickets

Create a sheet/tab named:

Tickets

Add the following headers in the first row:

timestamp  
ticket_title  
summary  
category  
priority  
security_risk  
business_impact  
recommended_actions  
suggested_user_response  
internal_technical_note  
needs_human_review  
status  
ticket_id  
sla_target  
assigned_queue  
escalation_required  

## n8n Workflow Setup

Create a new workflow with the following nodes:

- When chat message received
- AI Agent
- Code in JavaScript
- Google Sheets
- Gmail
- Chat: Send a message

## Google Sheets Node

Use the operation to append a new row.

Map the fields from the Code node to the spreadsheet columns.

## Gmail Node

Use Gmail to send a formatted email summary to the analyst.

Recommended email subject:

[Priority] Ticket Title

## Security Notes

Do not upload API keys, OAuth credentials, tokens, passwords, or secrets to GitHub.

Before publishing the workflow JSON, review the exported file and confirm that no sensitive credentials are included.

## Future Improvements

- Add conditional logic for sending email only when escalation is required
- Add approval step for access requests
- Add Microsoft Teams notification
- Add dashboard or reporting workflow
- Add knowledge base integration using Dify or Langflow
- Add real helpdesk integration such as Jira, ServiceNow, Zendesk, or Freshservice
