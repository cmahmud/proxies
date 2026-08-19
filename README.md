# SyndProxy private pool

## Current pool

- Alive now: 1064
- Gold now: 484
- HTTP: 366 alive / 136 gold
- HTTPS: 261 alive / 79 gold
- SOCKS4: 211 alive / 120 gold
- SOCKS5: 226 alive / 149 gold

## Historical pool

- Discovered: 119695
- Ever alive: 17866
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
