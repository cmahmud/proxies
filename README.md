# SyndProxy private pool

## Current pool

- Alive now: 1037
- Gold now: 401
- HTTP: 364 alive / 108 gold
- HTTPS: 234 alive / 23 gold
- SOCKS4: 219 alive / 149 gold
- SOCKS5: 220 alive / 121 gold

## Historical pool

- Discovered: 153722
- Ever alive: 28546
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
