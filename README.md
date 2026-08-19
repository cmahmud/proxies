# SyndProxy private pool

## Current pool

- Alive now: 1145
- Gold now: 499
- HTTP: 391 alive / 123 gold
- HTTPS: 247 alive / 74 gold
- SOCKS4: 233 alive / 149 gold
- SOCKS5: 274 alive / 153 gold

## Historical pool

- Discovered: 114411
- Ever alive: 17026
- Ever gold: 627

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
