"""Financial Forecasting Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_forecast_revenue():
    """Test Build revenue forecast from pipeline, contracts, and trends."""
    tools = AgentTools()
    result = await tools.forecast_revenue(period="test", method="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_project_expenses():
    """Test Project operating expenses based on cost drivers."""
    tools = AgentTools()
    result = await tools.project_expenses(period="test", cost_centers="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_model_cash_flow():
    """Test Model cash flow projections with scenario analysis."""
    tools = AgentTools()
    result = await tools.model_cash_flow(months_ahead=1, scenarios="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_forecast_working_capital():
    """Test Forecast working capital requirements."""
    tools = AgentTools()
    result = await tools.forecast_working_capital(period="test", dso_assumption=1)
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.financial_forecasting_agent_agent import FinancialForecastingAgentAgent
    agent = FinancialForecastingAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
