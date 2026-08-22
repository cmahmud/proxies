# SyndProxy private pool

## Current pool

- Alive now: 1075
- Gold now: 362
- HTTP: 408 alive / 74 gold
- HTTPS: 225 alive / 25 gold
- SOCKS4: 219 alive / 135 gold
- SOCKS5: 223 alive / 128 gold

## Historical pool

- Discovered: 165836
- Ever alive: 32360
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
