# SyndProxy private pool

## Current pool

- Alive now: 930
- Gold now: 285
- HTTP: 296 alive / 65 gold
- HTTPS: 235 alive / 18 gold
- SOCKS4: 206 alive / 102 gold
- SOCKS5: 193 alive / 100 gold

## Historical pool

- Discovered: 109961
- Ever alive: 15409
- Ever gold: 496

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
