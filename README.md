# SyndProxy private pool

## Current pool

- Alive now: 1124
- Gold now: 286
- HTTP: 464 alive / 27 gold
- HTTPS: 219 alive / 7 gold
- SOCKS4: 215 alive / 130 gold
- SOCKS5: 226 alive / 122 gold

## Historical pool

- Discovered: 102839
- Ever alive: 13108
- Ever gold: 412

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
