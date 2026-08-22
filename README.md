# SyndProxy private pool

## Current pool

- Alive now: 1007
- Gold now: 408
- HTTP: 348 alive / 79 gold
- HTTPS: 207 alive / 27 gold
- SOCKS4: 208 alive / 136 gold
- SOCKS5: 244 alive / 166 gold

## Historical pool

- Discovered: 163875
- Ever alive: 32029
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
