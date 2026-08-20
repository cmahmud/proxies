# SyndProxy private pool

## Current pool

- Alive now: 1385
- Gold now: 582
- HTTP: 509 alive / 195 gold
- HTTPS: 355 alive / 100 gold
- SOCKS4: 237 alive / 140 gold
- SOCKS5: 284 alive / 147 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23313
- Ever gold: 917

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
