# SyndProxy private pool

## Current pool

- Alive now: 915
- Gold now: 405
- HTTP: 286 alive / 82 gold
- HTTPS: 156 alive / 27 gold
- SOCKS4: 239 alive / 151 gold
- SOCKS5: 234 alive / 145 gold

## Historical pool

- Discovered: 165872
- Ever alive: 32378
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
