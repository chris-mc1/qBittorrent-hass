"""Fixtures for testing."""

from __future__ import annotations

from typing import TYPE_CHECKING
from unittest.mock import AsyncMock, patch

import pytest
from custom_components.qbittorrent_alt import helpers

if TYPE_CHECKING:
    from collections.abc import Generator


@pytest.fixture(autouse=True)
def auto_enable_custom_integrations(enable_custom_integrations: None) -> Generator:  # noqa: ARG001
    yield


@pytest.fixture
def mock_setup_client() -> Generator[AsyncMock]:
    with patch(
        "custom_components.qbittorrent_alt.config_flow.setup_client",
        AsyncMock(return_value=AsyncMock()),
    ) as mock_setup_client:
        yield mock_setup_client
