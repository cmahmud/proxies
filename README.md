# SyndProxy private pool

## Current pool

- Alive now: 1504
- Gold now: 607
- HTTP: 533 alive / 200 gold
- HTTPS: 430 alive / 98 gold
- SOCKS4: 239 alive / 147 gold
- SOCKS5: 302 alive / 162 gold

## Historical pool

- Discovered: 140459
- Ever alive: 23601
- Ever gold: 924

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
