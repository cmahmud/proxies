# SyndProxy private pool

## Current pool

- Alive now: 1203
- Gold now: 599
- HTTP: 423 alive / 188 gold
- HTTPS: 298 alive / 100 gold
- SOCKS4: 231 alive / 146 gold
- SOCKS5: 251 alive / 165 gold

## Historical pool

- Discovered: 138957
- Ever alive: 23467
- Ever gold: 922

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
