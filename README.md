# SyndProxy private pool

## Current pool

- Alive now: 1152
- Gold now: 499
- HTTP: 388 alive / 124 gold
- HTTPS: 262 alive / 75 gold
- SOCKS4: 233 alive / 149 gold
- SOCKS5: 269 alive / 151 gold

## Historical pool

- Discovered: 114412
- Ever alive: 17027
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
