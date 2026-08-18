# SyndProxy private pool

## Current pool

- Alive now: 981
- Gold now: 309
- HTTP: 374 alive / 30 gold
- HTTPS: 159 alive / 5 gold
- SOCKS4: 230 alive / 144 gold
- SOCKS5: 218 alive / 130 gold

## Historical pool

- Discovered: 102848
- Ever alive: 13349
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
