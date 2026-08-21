# SyndProxy private pool

## Current pool

- Alive now: 1326
- Gold now: 432
- HTTP: 512 alive / 106 gold
- HTTPS: 339 alive / 30 gold
- SOCKS4: 235 alive / 150 gold
- SOCKS5: 240 alive / 146 gold

## Historical pool

- Discovered: 160011
- Ever alive: 30514
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
