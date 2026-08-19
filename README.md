# SyndProxy private pool

## Current pool

- Alive now: 1210
- Gold now: 504
- HTTP: 403 alive / 124 gold
- HTTPS: 293 alive / 75 gold
- SOCKS4: 239 alive / 153 gold
- SOCKS5: 275 alive / 152 gold

## Historical pool

- Discovered: 114412
- Ever alive: 17029
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
