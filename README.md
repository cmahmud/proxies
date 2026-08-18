# SyndProxy private pool

## Current pool

- Alive now: 930
- Gold now: 304
- HTTP: 354 alive / 28 gold
- HTTPS: 139 alive / 6 gold
- SOCKS4: 224 alive / 142 gold
- SOCKS5: 213 alive / 128 gold

## Historical pool

- Discovered: 102848
- Ever alive: 13351
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
