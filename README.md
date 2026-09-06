# SyndProxy validated proxy pool

## Current pool

- Alive now: 422
- Gold now: 348
- HTTP: 75 alive / 61 gold
- HTTPS: 31 alive / 14 gold
- SOCKS4: 149 alive / 139 gold
- SOCKS5: 167 alive / 134 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48398
- Ever gold: 1531

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
