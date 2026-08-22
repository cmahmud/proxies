# SyndProxy private pool

## Current pool

- Alive now: 1041
- Gold now: 374
- HTTP: 348 alive / 80 gold
- HTTPS: 282 alive / 25 gold
- SOCKS4: 189 alive / 125 gold
- SOCKS5: 222 alive / 144 gold

## Historical pool

- Discovered: 165812
- Ever alive: 32317
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
