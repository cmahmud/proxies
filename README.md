# SyndProxy private pool

## Current pool

- Alive now: 1016
- Gold now: 362
- HTTP: 351 alive / 77 gold
- HTTPS: 236 alive / 22 gold
- SOCKS4: 213 alive / 135 gold
- SOCKS5: 216 alive / 128 gold

## Historical pool

- Discovered: 165836
- Ever alive: 32359
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
