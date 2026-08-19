# SyndProxy private pool

## Current pool

- Alive now: 1029
- Gold now: 395
- HTTP: 334 alive / 72 gold
- HTTPS: 212 alive / 15 gold
- SOCKS4: 249 alive / 148 gold
- SOCKS5: 234 alive / 160 gold

## Historical pool

- Discovered: 129319
- Ever alive: 20456
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
