# SyndProxy private pool

## Current pool

- Alive now: 892
- Gold now: 304
- HTTP: 294 alive / 63 gold
- HTTPS: 220 alive / 18 gold
- SOCKS4: 188 alive / 118 gold
- SOCKS5: 190 alive / 105 gold

## Historical pool

- Discovered: 109961
- Ever alive: 15418
- Ever gold: 497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
