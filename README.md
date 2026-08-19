# SyndProxy private pool

## Current pool

- Alive now: 1068
- Gold now: 461
- HTTP: 377 alive / 125 gold
- HTTPS: 279 alive / 79 gold
- SOCKS4: 211 alive / 143 gold
- SOCKS5: 201 alive / 114 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17457
- Ever gold: 664

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
