# SyndProxy private pool

## Current pool

- Alive now: 796
- Gold now: 383
- HTTP: 188 alive / 77 gold
- HTTPS: 203 alive / 21 gold
- SOCKS4: 202 alive / 134 gold
- SOCKS5: 203 alive / 151 gold

## Historical pool

- Discovered: 151055
- Ever alive: 27203
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
