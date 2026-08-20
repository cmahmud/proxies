# SyndProxy private pool

## Current pool

- Alive now: 1339
- Gold now: 583
- HTTP: 493 alive / 195 gold
- HTTPS: 341 alive / 100 gold
- SOCKS4: 234 alive / 141 gold
- SOCKS5: 271 alive / 147 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23311
- Ever gold: 917

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
