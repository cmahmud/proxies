# SyndProxy private pool

## Current pool

- Alive now: 1035
- Gold now: 534
- HTTP: 368 alive / 156 gold
- HTTPS: 238 alive / 89 gold
- SOCKS4: 211 alive / 149 gold
- SOCKS5: 218 alive / 140 gold

## Historical pool

- Discovered: 119811
- Ever alive: 18036
- Ever gold: 712

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
