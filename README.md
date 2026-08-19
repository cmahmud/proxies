# SyndProxy private pool

## Current pool

- Alive now: 1176
- Gold now: 553
- HTTP: 446 alive / 190 gold
- HTTPS: 278 alive / 105 gold
- SOCKS4: 239 alive / 119 gold
- SOCKS5: 213 alive / 139 gold

## Historical pool

- Discovered: 124836
- Ever alive: 19293
- Ever gold: 771

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
