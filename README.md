# SyndProxy private pool

## Current pool

- Alive now: 796
- Gold now: 285
- HTTP: 261 alive / 36 gold
- HTTPS: 153 alive / 9 gold
- SOCKS4: 205 alive / 140 gold
- SOCKS5: 177 alive / 100 gold

## Historical pool

- Discovered: 102931
- Ever alive: 13961
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
