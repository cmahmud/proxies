# SyndProxy private pool

## Current pool

- Alive now: 938
- Gold now: 326
- HTTP: 281 alive / 55 gold
- HTTPS: 204 alive / 9 gold
- SOCKS4: 230 alive / 138 gold
- SOCKS5: 223 alive / 124 gold

## Historical pool

- Discovered: 129276
- Ever alive: 20264
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
