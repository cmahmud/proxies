# SyndProxy private pool

## Current pool

- Alive now: 1129
- Gold now: 494
- HTTP: 408 alive / 120 gold
- HTTPS: 239 alive / 74 gold
- SOCKS4: 225 alive / 147 gold
- SOCKS5: 257 alive / 153 gold

## Historical pool

- Discovered: 114411
- Ever alive: 16976
- Ever gold: 627

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
