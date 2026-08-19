# SyndProxy private pool

## Current pool

- Alive now: 1027
- Gold now: 352
- HTTP: 360 alive / 71 gold
- HTTPS: 219 alive / 18 gold
- SOCKS4: 201 alive / 120 gold
- SOCKS5: 247 alive / 143 gold

## Historical pool

- Discovered: 110856
- Ever alive: 15773
- Ever gold: 504

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
