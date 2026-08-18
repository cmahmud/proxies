# SyndProxy private pool

## Current pool

- Alive now: 1011
- Gold now: 281
- HTTP: 352 alive / 33 gold
- HTTPS: 220 alive / 5 gold
- SOCKS4: 219 alive / 134 gold
- SOCKS5: 220 alive / 109 gold

## Historical pool

- Discovered: 99074
- Ever alive: 11399
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
