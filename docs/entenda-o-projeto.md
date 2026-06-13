# Entenda o projeto sem complicação

## A ideia central

O AI Rapid Triage Agent funciona como um assistente de primeira triagem para o suporte de TI.

Ele não resolve o chamado sozinho. O objetivo é organizar a solicitação antes que um analista humano assuma o atendimento.

## O que acontece quando o usuário escreve no chat

1. O chat recebe a descrição do problema.
2. O agente de IA identifica categoria, prioridade, risco e impacto.
3. O JavaScript transforma o texto em campos separados.
4. O Google Sheets registra os dados do chamado.
5. O Gmail envia um resumo ao analista.
6. O chat apresenta o resultado da triagem.

## O que é cada tecnologia

### n8n
É a plataforma que conecta todas as etapas. Cada caixa visual é chamada de node.

### AI Agent
É o node que interpreta a solicitação e produz a primeira análise.

### OpenAI Chat Model
É o modelo de linguagem utilizado pelo AI Agent.

### JavaScript Code Node
É a etapa que limpa a resposta e cria campos como ticket ID, SLA e fila responsável.

### Google Sheets
Funciona como uma base simples para registrar e acompanhar os tickets.

### Gmail
Envia o resumo da triagem para o analista.

## Por que existe revisão humana

A IA pode interpretar uma mensagem incorretamente, definir uma prioridade inadequada ou deixar de perceber um detalhe importante. Por isso, o projeto trata a IA como apoio ao analista, e não como substituta da decisão humana.

## Frase simples para explicar o projeto

> Criei um workflow no n8n que recebe uma solicitação de suporte, usa IA para fazer a primeira triagem, registra o ticket no Google Sheets e envia um resumo por e-mail para o analista.
