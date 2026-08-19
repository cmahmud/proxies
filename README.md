# SyndProxy private pool

## Current pool

- Alive now: 1206
- Gold now: 501
- HTTP: 396 alive / 124 gold
- HTTPS: 287 alive / 73 gold
- SOCKS4: 249 alive / 153 gold
- SOCKS5: 274 alive / 151 gold

## Historical pool

- Discovered: 114412
- Ever alive: 17030
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
