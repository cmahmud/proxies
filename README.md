# SyndProxy private pool

## Current pool

- Alive now: 1068
- Gold now: 284
- HTTP: 371 alive / 27 gold
- HTTPS: 217 alive / 4 gold
- SOCKS4: 235 alive / 135 gold
- SOCKS5: 245 alive / 118 gold

## Historical pool

- Discovered: 102805
- Ever alive: 12708
- Ever gold: 399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
