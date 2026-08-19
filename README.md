# SyndProxy private pool

## Current pool

- Alive now: 1387
- Gold now: 405
- HTTP: 514 alive / 78 gold
- HTTPS: 318 alive / 16 gold
- SOCKS4: 245 alive / 156 gold
- SOCKS5: 310 alive / 155 gold

## Historical pool

- Discovered: 134523
- Ever alive: 21911
- Ever gold: 888

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
