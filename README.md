# SyndProxy private pool

## Current pool

- Alive now: 1293
- Gold now: 403
- HTTP: 440 alive / 77 gold
- HTTPS: 277 alive / 14 gold
- SOCKS4: 302 alive / 150 gold
- SOCKS5: 274 alive / 162 gold

## Historical pool

- Discovered: 131116
- Ever alive: 20668
- Ever gold: 871

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
