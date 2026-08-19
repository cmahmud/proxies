# SyndProxy private pool

## Current pool

- Alive now: 1012
- Gold now: 377
- HTTP: 347 alive / 72 gold
- HTTPS: 218 alive / 19 gold
- SOCKS4: 200 alive / 126 gold
- SOCKS5: 247 alive / 160 gold

## Historical pool

- Discovered: 110856
- Ever alive: 15763
- Ever gold: 504

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
