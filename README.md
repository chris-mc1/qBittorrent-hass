# qBittorrent Alt

Alternative qBittorrent Integration for Home Assistant

## Installation

You can install this integration via [HACS](#hacs) or [manually](#manual).

### HACS

### Installation through HACS

1. If HACS is not installed, follow HACS installation and configuration at <https://hacs.xyz/>.

2. Click the button below or visit HACS and search for "qBittorrent Alt".

    [![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=chris-mc1&repository=qBittorrent-hass&category=integrations)

3. Install the integration.

4. Restart Home Assistant!

### Manual

Copy the `custom_components/qbittorrent_alt` folder to your custom_components folder. Then Reboot Home Assistant.

## Configuration

* Click the button below or use "Add Integration" in Home Assistant and select "qBittorrent Alt".

    [![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=qbittorrent_alt)

* Enter the URL ( including the "http(s)" ) and a Name for your qBittorrent instance.
If authentication is enabled, enter your Username and Password, otherwise leave them empty. When using a self-signed Certificate uncheck "Verify SSL certificate".

## Available components

### Sensors

* Status (up_down, seeding, downloading, idle)
* Connection State (connected, firewalled, disconnected)
* Upload / Download Speed
* Uploaded / Downloaded this Session
* Uploaded / Downloaded total
* Global share Ratio
* Number of Torrents Downloading / Seeding / Uploading / Paused / Stalled / Total
* ETA

### Switch

* Alternative Speed Switch

### Number

* Normal Up / Down Limit
* Alternative Up / Down Limit
* Current Up / Down Limit
* Listening Port

### Button

* Pause all Torrents
* Resume all Torrents

### Actions

* Pause / resume torrents

    Pause or resume a specific torrent using the torrent hash
* Get torrent info

    Returns detailed torrent information on a specific torrent or all torrents. When requesting all, torrents can be filter by state.
