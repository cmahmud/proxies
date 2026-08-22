# SyndProxy private pool

## Current pool

- Alive now: 939
- Gold now: 425
- HTTP: 295 alive / 98 gold
- HTTPS: 218 alive / 31 gold
- SOCKS4: 196 alive / 137 gold
- SOCKS5: 230 alive / 159 gold

## Historical pool

- Discovered: 161016
- Ever alive: 31086
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
