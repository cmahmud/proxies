# SyndProxy private pool

## Current pool

- Alive now: 1043
- Gold now: 475
- HTTP: 341 alive / 121 gold
- HTTPS: 253 alive / 72 gold
- SOCKS4: 231 alive / 140 gold
- SOCKS5: 218 alive / 142 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16547
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
