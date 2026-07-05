# Financial Forecasting Agent

[![CI](https://github.com/kogunlowo123/financial-forecasting-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/financial-forecasting-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Finance | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Financial forecasting agent that builds revenue and expense projections, models cash flow scenarios, forecasts working capital needs, and provides budget variance predictions.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `forecast_revenue` | Build revenue forecast from pipeline, contracts, and trends |
| `project_expenses` | Project operating expenses based on cost drivers |
| `model_cash_flow` | Model cash flow projections with scenario analysis |
| `forecast_working_capital` | Forecast working capital requirements |
| `predict_variance` | Predict budget variance based on current run rates |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/financial-forecasting/process` | Process transaction |
| `POST` | `/api/v1/financial-forecasting/analyze` | Analyze data |
| `POST` | `/api/v1/financial-forecasting/validate` | Validate |
| `POST` | `/api/v1/financial-forecasting/report` | Generate report |
| `GET` | `/api/v1/financial-forecasting/audit` | Get audit trail |

## Features

- Financial
- Forecasting
- Compliance
- Reporting

## Integrations

- Netsuite
- Quickbooks
- Xero
- Sap
- Oracle Financials

## Architecture

```
financial-forecasting-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── financial_forecasting_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**ERP + Accounting Platform + LLM**

---

Built as part of the Enterprise AI Agent Platform.
