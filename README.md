# SyndProxy private pool

## Current pool

- Alive now: 909
- Gold now: 280
- HTTP: 324 alive / 38 gold
- HTTPS: 201 alive / 10 gold
- SOCKS4: 222 alive / 140 gold
- SOCKS5: 162 alive / 92 gold

## Historical pool

- Discovered: 102917
- Ever alive: 13932
- Ever gold: 433

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
