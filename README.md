# SyndProxy private pool

## Current pool

- Alive now: 1043
- Gold now: 277
- HTTP: 355 alive / 25 gold
- HTTPS: 234 alive / 5 gold
- SOCKS4: 223 alive / 125 gold
- SOCKS5: 231 alive / 122 gold

## Historical pool

- Discovered: 102838
- Ever alive: 13085
- Ever gold: 412

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
