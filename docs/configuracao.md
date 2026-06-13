# Guia de configuração

## Requisitos

- conta no n8n ou instância self-hosted;
- credencial da OpenAI configurada no n8n;
- credencial do Google Sheets;
- credencial do Gmail;
- planilha para armazenar os tickets.

## Importar o workflow

1. Abra o n8n.
2. Crie um novo workflow.
3. Escolha a opção de importar arquivo.
4. Selecione `workflow/ai-rapid-triage-agent.json`.
5. Abra cada node com credenciais e selecione sua própria conexão.

## Configurar o Google Sheets

Crie uma planilha com uma aba chamada `Tickets`.

Na primeira linha, adicione estas colunas:

```text
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
```

Depois, no node **Append row in sheet**:

1. selecione sua credencial;
2. informe o ID da planilha;
3. selecione a aba `Tickets`;
4. confirme o mapeamento das colunas.

## Configurar o Gmail

No node **Send a message**:

1. selecione sua credencial do Gmail;
2. substitua `analyst@example.com` pelo endereço desejado;
3. revise o assunto e o corpo do e-mail.

## Configurar o modelo

No node **OpenAI Chat Model**:

1. selecione sua credencial da OpenAI;
2. escolha um modelo disponível na sua conta;
3. mantenha temperatura baixa para respostas mais consistentes.

## Testar

Use uma solicitação como:

```text
Não consigo acessar o e-mail corporativo. Minha conta parece bloqueada e não recebo o código do MFA.
```

Verifique se:

- o chat retorna uma triagem;
- uma nova linha aparece na planilha;
- o e-mail é enviado;
- prioridade, SLA e fila fazem sentido.

## Segurança

O arquivo público do workflow foi preparado como template e não contém credenciais reais, IDs pessoais de conexão, planilha particular ou endereço pessoal de destino.
