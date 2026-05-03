# Workflow Overview

## Workflow Name

AI Rapid Triage Agent

## High-Level Flow

When chat message received  
↓  
AI Agent  
↓  
Code in JavaScript  
↓  
Google Sheets  
↓  
Gmail  
↓  
Chat: Send a message  

## Node 1: Chat Trigger

The workflow starts when a user sends a support request through the n8n chat interface.

The input message is captured and passed to the AI Agent.

## Node 2: AI Agent

The AI Agent analyzes the support request and produces a triage report using a predefined structure.

The agent identifies:

- Ticket title
- Issue summary
- Category
- Priority
- Security risk
- Business impact
- Recommended actions
- Suggested user response
- Internal technical note
- Human review requirement

## Node 3: Code in JavaScript

The Code node cleans the AI output and extracts each field into structured JSON properties.

It also generates additional operational fields:

- Timestamp
- Ticket ID
- SLA target
- Assigned queue
- Escalation requirement
- Ticket status

## Node 4: Google Sheets

The Google Sheets node appends a new row to the ticket tracking spreadsheet.

The spreadsheet stores all triaged requests for tracking and analysis.

## Node 5: Gmail

The Gmail node sends a formatted email summary to the analyst.

The email includes ticket metadata, summary, business impact, recommended actions, suggested user response, and internal technical notes.

## Node 6: Chat Response

The final Chat node sends a response back to the n8n chat confirming that the ticket was registered and the email was sent.

## Data Output Example

Ticket ID: TRIAGE-20260503-213138  
Title: Request for access to a shared finance folder  
Category: Access Request  
Priority: Medium  
Security Risk: None  
SLA: 1 business day  
Assigned Queue: Identity & Access Support  
Status: New  
