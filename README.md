# SyndProxy private pool

## Current pool

- Alive now: 1088
- Gold now: 524
- HTTP: 434 alive / 179 gold
- HTTPS: 259 alive / 98 gold
- SOCKS4: 202 alive / 117 gold
- SOCKS5: 193 alive / 130 gold

## Historical pool

- Discovered: 124851
- Ever alive: 19404
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
