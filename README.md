# SyndProxy private pool

## Current pool

- Alive now: 1182
- Gold now: 481
- HTTP: 461 alive / 190 gold
- HTTPS: 297 alive / 112 gold
- SOCKS4: 215 alive / 78 gold
- SOCKS5: 209 alive / 101 gold

## Historical pool

- Discovered: 124845
- Ever alive: 19388
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
