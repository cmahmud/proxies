# SyndProxy private pool

## Current pool

- Alive now: 974
- Gold now: 387
- HTTP: 298 alive / 75 gold
- HTTPS: 217 alive / 21 gold
- SOCKS4: 220 alive / 145 gold
- SOCKS5: 239 alive / 146 gold

## Historical pool

- Discovered: 156741
- Ever alive: 29578
- Ever gold: 1132

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
