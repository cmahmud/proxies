# SyndProxy private pool

## Current pool

- Alive now: 813
- Gold now: 278
- HTTP: 291 alive / 37 gold
- HTTPS: 148 alive / 8 gold
- SOCKS4: 209 alive / 138 gold
- SOCKS5: 165 alive / 95 gold

## Historical pool

- Discovered: 102915
- Ever alive: 13931
- Ever gold: 432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
