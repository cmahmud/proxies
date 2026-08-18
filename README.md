# SyndProxy private pool

## Current pool

- Alive now: 944
- Gold now: 311
- HTTP: 322 alive / 32 gold
- HTTPS: 180 alive / 5 gold
- SOCKS4: 224 alive / 145 gold
- SOCKS5: 218 alive / 129 gold

## Historical pool

- Discovered: 102848
- Ever alive: 13284
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
