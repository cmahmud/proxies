# SyndProxy validated proxy pool

## Current pool

- Alive now: 422
- Gold now: 342
- HTTP: 85 alive / 63 gold
- HTTPS: 38 alive / 13 gold
- SOCKS4: 151 alive / 139 gold
- SOCKS5: 148 alive / 127 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48374
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
