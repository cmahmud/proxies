# SyndProxy private pool

## Current pool

- Alive now: 1492
- Gold now: 381
- HTTP: 535 alive / 101 gold
- HTTPS: 408 alive / 21 gold
- SOCKS4: 237 alive / 116 gold
- SOCKS5: 312 alive / 143 gold

## Historical pool

- Discovered: 136221
- Ever alive: 22483
- Ever gold: 907

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
