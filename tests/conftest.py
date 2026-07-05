"""Test configuration for Financial Forecasting Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "financial-forecasting-agent", "category": "Finance"}
