# SyndProxy private pool

## Current pool

- Alive now: 1065
- Gold now: 445
- HTTP: 327 alive / 94 gold
- HTTPS: 218 alive / 30 gold
- SOCKS4: 240 alive / 150 gold
- SOCKS5: 280 alive / 171 gold

## Historical pool

- Discovered: 161016
- Ever alive: 31030
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
