# SyndProxy private pool

## Current pool

- Alive now: 1277
- Gold now: 422
- HTTP: 478 alive / 97 gold
- HTTPS: 361 alive / 27 gold
- SOCKS4: 201 alive / 140 gold
- SOCKS5: 237 alive / 158 gold

## Historical pool

- Discovered: 159278
- Ever alive: 30398
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
