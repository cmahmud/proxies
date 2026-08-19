# SyndProxy private pool

## Current pool

- Alive now: 1352
- Gold now: 415
- HTTP: 455 alive / 85 gold
- HTTPS: 348 alive / 17 gold
- SOCKS4: 233 alive / 157 gold
- SOCKS5: 316 alive / 156 gold

## Historical pool

- Discovered: 134522
- Ever alive: 21831
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
