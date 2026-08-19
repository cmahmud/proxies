# SyndProxy private pool

## Current pool

- Alive now: 1155
- Gold now: 388
- HTTP: 375 alive / 89 gold
- HTTPS: 227 alive / 15 gold
- SOCKS4: 248 alive / 144 gold
- SOCKS5: 305 alive / 140 gold

## Historical pool

- Discovered: 133967
- Ever alive: 21701
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
