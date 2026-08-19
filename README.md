# SyndProxy private pool

## Current pool

- Alive now: 1043
- Gold now: 500
- HTTP: 333 alive / 138 gold
- HTTPS: 260 alive / 81 gold
- SOCKS4: 237 alive / 150 gold
- SOCKS5: 213 alive / 131 gold

## Historical pool

- Discovered: 119697
- Ever alive: 17902
- Ever gold: 705

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
