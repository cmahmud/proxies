# SyndProxy private pool

## Current pool

- Alive now: 855
- Gold now: 377
- HTTP: 238 alive / 70 gold
- HTTPS: 174 alive / 21 gold
- SOCKS4: 219 alive / 140 gold
- SOCKS5: 224 alive / 146 gold

## Historical pool

- Discovered: 144768
- Ever alive: 25269
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
