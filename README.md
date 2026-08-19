# SyndProxy private pool

## Current pool

- Alive now: 1326
- Gold now: 399
- HTTP: 452 alive / 92 gold
- HTTPS: 296 alive / 15 gold
- SOCKS4: 255 alive / 147 gold
- SOCKS5: 323 alive / 145 gold

## Historical pool

- Discovered: 133967
- Ever alive: 21692
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
