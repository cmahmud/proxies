# SyndProxy private pool

## Current pool

- Alive now: 1386
- Gold now: 413
- HTTP: 468 alive / 86 gold
- HTTPS: 375 alive / 16 gold
- SOCKS4: 233 alive / 157 gold
- SOCKS5: 310 alive / 154 gold

## Historical pool

- Discovered: 134458
- Ever alive: 21822
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
