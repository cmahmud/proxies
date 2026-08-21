# SyndProxy private pool

## Current pool

- Alive now: 1197
- Gold now: 431
- HTTP: 416 alive / 108 gold
- HTTPS: 304 alive / 28 gold
- SOCKS4: 224 alive / 150 gold
- SOCKS5: 253 alive / 145 gold

## Historical pool

- Discovered: 153722
- Ever alive: 28557
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
