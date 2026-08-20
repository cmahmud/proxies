# SyndProxy private pool

## Current pool

- Alive now: 1503
- Gold now: 636
- HTTP: 562 alive / 234 gold
- HTTPS: 464 alive / 119 gold
- SOCKS4: 226 alive / 145 gold
- SOCKS5: 251 alive / 138 gold

## Historical pool

- Discovered: 142747
- Ever alive: 24643
- Ever gold: 1029

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
