# SyndProxy private pool

## Current pool

- Alive now: 1022
- Gold now: 511
- HTTP: 341 alive / 142 gold
- HTTPS: 243 alive / 85 gold
- SOCKS4: 231 alive / 149 gold
- SOCKS5: 207 alive / 135 gold

## Historical pool

- Discovered: 119808
- Ever alive: 17941
- Ever gold: 705

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
