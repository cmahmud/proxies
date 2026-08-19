# SyndProxy private pool

## Current pool

- Alive now: 1044
- Gold now: 499
- HTTP: 334 alive / 138 gold
- HTTPS: 260 alive / 80 gold
- SOCKS4: 240 alive / 150 gold
- SOCKS5: 210 alive / 131 gold

## Historical pool

- Discovered: 119697
- Ever alive: 17902
- Ever gold: 705

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
