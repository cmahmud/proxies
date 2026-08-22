# SyndProxy private pool

## Current pool

- Alive now: 829
- Gold now: 407
- HTTP: 207 alive / 90 gold
- HTTPS: 170 alive / 29 gold
- SOCKS4: 219 alive / 134 gold
- SOCKS5: 233 alive / 154 gold

## Historical pool

- Discovered: 163855
- Ever alive: 31948
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
