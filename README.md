# SyndProxy private pool

## Current pool

- Alive now: 872
- Gold now: 283
- HTTP: 291 alive / 40 gold
- HTTPS: 150 alive / 9 gold
- SOCKS4: 242 alive / 139 gold
- SOCKS5: 189 alive / 95 gold

## Historical pool

- Discovered: 102895
- Ever alive: 13844
- Ever gold: 431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
