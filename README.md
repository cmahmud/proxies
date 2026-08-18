# SyndProxy private pool

## Current pool

- Alive now: 1050
- Gold now: 320
- HTTP: 351 alive / 42 gold
- HTTPS: 214 alive / 11 gold
- SOCKS4: 246 alive / 138 gold
- SOCKS5: 239 alive / 129 gold

## Historical pool

- Discovered: 107044
- Ever alive: 14405
- Ever gold: 443

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
