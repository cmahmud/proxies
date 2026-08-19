# SyndProxy private pool

## Current pool

- Alive now: 1340
- Gold now: 415
- HTTP: 449 alive / 87 gold
- HTTPS: 356 alive / 17 gold
- SOCKS4: 227 alive / 157 gold
- SOCKS5: 308 alive / 154 gold

## Historical pool

- Discovered: 134458
- Ever alive: 21822
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
