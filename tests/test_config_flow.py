from __future__ import annotations

from typing import TYPE_CHECKING
from unittest.mock import AsyncMock, Mock

from aiohttp import ClientConnectorError
from aioqbt.exc import LoginError
from custom_components.qbittorrent_alt.const import DOMAIN
from homeassistant.config_entries import SOURCE_USER
from homeassistant.const import (
    CONF_NAME,
    CONF_PASSWORD,
    CONF_URL,
    CONF_USERNAME,
    CONF_VERIFY_SSL,
)
from homeassistant.data_entry_flow import FlowResultType

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant


async def test_user_init(hass: HomeAssistant, mock_setup_client: AsyncMock) -> None:
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": SOURCE_USER}
    )

    assert result["type"] is FlowResultType.FORM
    assert result["step_id"] == "user"
    assert not result["errors"]

    result = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        user_input={
            CONF_URL: "http://1.2.3.4",
            CONF_NAME: "qBit",
            CONF_VERIFY_SSL: False,
        },
    )

    mock_setup_client.assert_awaited_once_with(
        "http://1.2.3.4/api/v2", None, None, False
    )

    mock_setup_client.return_value.close.assert_awaited_once()

    assert result["type"] is FlowResultType.CREATE_ENTRY
    assert result["title"] == "qBit"
    assert result["data"][CONF_URL] == "http://1.2.3.4"
    assert result["data"][CONF_NAME] == "qBit"
    assert result["data"][CONF_VERIFY_SSL] is False
    assert CONF_USERNAME not in result["data"]
    assert CONF_PASSWORD not in result["data"]
    assert "errors" not in result


async def test_user_init_password(
    hass: HomeAssistant, mock_setup_client: AsyncMock
) -> None:
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": SOURCE_USER}
    )

    assert result["type"] is FlowResultType.FORM
    assert result["step_id"] == "user"
    assert not result["errors"]

    result = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        user_input={
            CONF_URL: "http://1.2.3.4",
            CONF_NAME: "qBit",
            CONF_VERIFY_SSL: False,
            CONF_USERNAME: "username",
            CONF_PASSWORD: "password",
        },
    )

    mock_setup_client.assert_awaited_once_with(
        "http://1.2.3.4/api/v2", "username", "password", False
    )

    mock_setup_client.return_value.close.assert_awaited_once()

    assert result["type"] is FlowResultType.CREATE_ENTRY
    assert result["title"] == "qBit"
    assert result["data"][CONF_URL] == "http://1.2.3.4"
    assert result["data"][CONF_NAME] == "qBit"
    assert result["data"][CONF_VERIFY_SSL] is False
    assert result["data"][CONF_USERNAME] == "username"
    assert result["data"][CONF_PASSWORD] == "password"
    assert "errors" not in result


async def test_user_only_password(hass: HomeAssistant) -> None:
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": SOURCE_USER}
    )

    assert result["type"] is FlowResultType.FORM
    assert result["step_id"] == "user"
    assert not result["errors"]

    result = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        user_input={
            CONF_URL: "http://1.2.3.4",
            CONF_NAME: "qBit",
            CONF_VERIFY_SSL: False,
            CONF_PASSWORD: "password",
        },
    )

    assert result["type"] is FlowResultType.FORM
    assert result["errors"] == {"base": "missing_password"}


async def test_user_only_username(hass: HomeAssistant) -> None:
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": SOURCE_USER}
    )

    assert result["type"] is FlowResultType.FORM
    assert result["step_id"] == "user"
    assert not result["errors"]

    result = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        user_input={
            CONF_URL: "http://1.2.3.4",
            CONF_NAME: "qBit",
            CONF_VERIFY_SSL: False,
            CONF_USERNAME: "username",
        },
    )

    assert result["type"] is FlowResultType.FORM
    assert result["errors"] == {"base": "missing_password"}


async def test_user_auth_failed(
    hass: HomeAssistant, mock_setup_client: AsyncMock
) -> None:
    mock_setup_client.side_effect = LoginError()

    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": SOURCE_USER}
    )

    assert result["type"] is FlowResultType.FORM
    assert result["step_id"] == "user"
    assert not result["errors"]

    result = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        user_input={
            CONF_URL: "http://1.2.3.4",
            CONF_NAME: "qBit",
            CONF_VERIFY_SSL: False,
        },
    )

    assert result["type"] is FlowResultType.FORM
    assert result["errors"] == {"base": "invalid_auth"}


async def test_user_connection_failed(
    hass: HomeAssistant, mock_setup_client: AsyncMock
) -> None:
    mock_setup_client.side_effect = ClientConnectorError(Mock(), Mock())

    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": SOURCE_USER}
    )

    assert result["type"] is FlowResultType.FORM
    assert result["step_id"] == "user"
    assert not result["errors"]

    result = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        user_input={
            CONF_URL: "http://1.2.3.4",
            CONF_NAME: "qBit",
            CONF_VERIFY_SSL: False,
        },
    )

    assert result["type"] is FlowResultType.FORM
    assert result["errors"] == {"base": "cannot_connect"}
