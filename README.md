# SyndProxy private pool

## Current pool

- Alive now: 1068
- Gold now: 403
- HTTP: 362 alive / 104 gold
- HTTPS: 295 alive / 27 gold
- SOCKS4: 199 alive / 148 gold
- SOCKS5: 212 alive / 124 gold

## Historical pool

- Discovered: 153184
- Ever alive: 28461
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
