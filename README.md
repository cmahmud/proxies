# SyndProxy private pool

## Current pool

- Alive now: 1016
- Gold now: 355
- HTTP: 312 alive / 66 gold
- HTTPS: 247 alive / 14 gold
- SOCKS4: 232 alive / 126 gold
- SOCKS5: 225 alive / 149 gold

## Historical pool

- Discovered: 129286
- Ever alive: 20270
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
