# SyndProxy private pool

## Current pool

- Alive now: 999
- Gold now: 374
- HTTP: 324 alive / 89 gold
- HTTPS: 267 alive / 25 gold
- SOCKS4: 186 alive / 120 gold
- SOCKS5: 222 alive / 140 gold

## Historical pool

- Discovered: 153749
- Ever alive: 28831
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
