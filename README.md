# SyndProxy private pool

## Current pool

- Alive now: 866
- Gold now: 252
- HTTP: 361 alive / 27 gold
- HTTPS: 103 alive / 2 gold
- SOCKS4: 189 alive / 117 gold
- SOCKS5: 213 alive / 106 gold

## Historical pool

- Discovered: 99104
- Ever alive: 11670
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
