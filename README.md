# SyndProxy private pool

## Current pool

- Alive now: 1063
- Gold now: 489
- HTTP: 367 alive / 122 gold
- HTTPS: 230 alive / 75 gold
- SOCKS4: 213 alive / 141 gold
- SOCKS5: 253 alive / 151 gold

## Historical pool

- Discovered: 114270
- Ever alive: 16918
- Ever gold: 627

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
