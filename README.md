# SyndProxy private pool

## Current pool

- Alive now: 1435
- Gold now: 564
- HTTP: 492 alive / 193 gold
- HTTPS: 413 alive / 89 gold
- SOCKS4: 234 alive / 150 gold
- SOCKS5: 296 alive / 132 gold

## Historical pool

- Discovered: 140459
- Ever alive: 23610
- Ever gold: 924

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
