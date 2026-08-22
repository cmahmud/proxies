# SyndProxy private pool

## Current pool

- Alive now: 882
- Gold now: 388
- HTTP: 276 alive / 89 gold
- HTTPS: 169 alive / 20 gold
- SOCKS4: 180 alive / 117 gold
- SOCKS5: 257 alive / 162 gold

## Historical pool

- Discovered: 166337
- Ever alive: 32396
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
