# SyndProxy private pool

## Current pool

- Alive now: 994
- Gold now: 432
- HTTP: 319 alive / 99 gold
- HTTPS: 191 alive / 28 gold
- SOCKS4: 225 alive / 146 gold
- SOCKS5: 259 alive / 159 gold

## Historical pool

- Discovered: 167127
- Ever alive: 32549
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
