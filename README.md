# SyndProxy private pool

## Current pool

- Alive now: 872
- Gold now: 383
- HTTP: 277 alive / 87 gold
- HTTPS: 176 alive / 27 gold
- SOCKS4: 211 alive / 139 gold
- SOCKS5: 208 alive / 130 gold

## Historical pool

- Discovered: 162762
- Ever alive: 31597
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
