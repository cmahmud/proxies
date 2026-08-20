# SyndProxy private pool

## Current pool

- Alive now: 1314
- Gold now: 582
- HTTP: 463 alive / 193 gold
- HTTPS: 327 alive / 101 gold
- SOCKS4: 247 alive / 141 gold
- SOCKS5: 277 alive / 147 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23300
- Ever gold: 917

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
