# qBittorrent Alt
Alternative qBittorrent Integration for Home Assistant

Adds the following features:
- Sensors:
    * Status (seeding, downloading, up_down)
    * Connection State (connected, firewalled, disconnected)
    * Upload and Download Speed
    * Uploaded and Downloaded Data (Session and Total)
    * Global share ratio
    * How many torrents are still in 'downloading' state
    * The longest ETA of all downloading torrents
- Alternative Speed Switch
- Number Entities:
    * Normal, Current and Alternative Speedlimit
    * Listening Port
- Button to Pause and Resume all torrents
- Services:
    * Pause/resume all torrents, or a specific torrent via an optional hash
    * Return information on all torrents, or a specific torrent via an optional hash