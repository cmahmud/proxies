# SyndProxy private pool

## Current pool

- Alive now: 1306
- Gold now: 415
- HTTP: 459 alive / 83 gold
- HTTPS: 289 alive / 16 gold
- SOCKS4: 289 alive / 151 gold
- SOCKS5: 269 alive / 165 gold

## Historical pool

- Discovered: 131116
- Ever alive: 20655
- Ever gold: 871

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
