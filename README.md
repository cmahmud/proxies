# SyndProxy private pool

## Current pool

- Alive now: 995
- Gold now: 498
- HTTP: 363 alive / 179 gold
- HTTPS: 234 alive / 100 gold
- SOCKS4: 213 alive / 108 gold
- SOCKS5: 185 alive / 111 gold

## Historical pool

- Discovered: 124845
- Ever alive: 19343
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
