# Visão geral do workflow

```text
Chat Trigger
→ AI Agent
→ JavaScript Code
→ Google Sheets
→ Gmail
→ Chat Response
```

## Função de cada etapa

- **Chat Trigger:** recebe a solicitação.
- **AI Agent:** identifica categoria, prioridade, risco e impacto.
- **JavaScript Code:** transforma a resposta em campos e adiciona ticket ID, SLA e fila.
- **Google Sheets:** registra o chamado.
- **Gmail:** envia o resumo ao analista.
- **Chat Response:** devolve o resultado ao usuário.

Mais detalhes estão no [README](./README.md).
