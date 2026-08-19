# SyndProxy private pool

## Current pool

- Alive now: 1009
- Gold now: 505
- HTTP: 373 alive / 182 gold
- HTTPS: 247 alive / 102 gold
- SOCKS4: 205 alive / 109 gold
- SOCKS5: 184 alive / 112 gold

## Historical pool

- Discovered: 124845
- Ever alive: 19373
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
