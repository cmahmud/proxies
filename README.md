# SyndProxy private pool

## Current pool

- Alive now: 808
- Gold now: 365
- HTTP: 239 alive / 63 gold
- HTTPS: 157 alive / 13 gold
- SOCKS4: 210 alive / 150 gold
- SOCKS5: 202 alive / 139 gold

## Historical pool

- Discovered: 147686
- Ever alive: 25904
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
