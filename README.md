# SyndProxy private pool

## Current pool

- Alive now: 1164
- Gold now: 493
- HTTP: 452 alive / 189 gold
- HTTPS: 297 alive / 112 gold
- SOCKS4: 205 alive / 82 gold
- SOCKS5: 210 alive / 110 gold

## Historical pool

- Discovered: 124845
- Ever alive: 19388
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
