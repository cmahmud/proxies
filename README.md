# SyndProxy private pool

## Current pool

- Alive now: 1295
- Gold now: 515
- HTTP: 498 alive / 188 gold
- HTTPS: 343 alive / 46 gold
- SOCKS4: 212 alive / 121 gold
- SOCKS5: 242 alive / 160 gold

## Historical pool

- Discovered: 125606
- Ever alive: 19577
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
