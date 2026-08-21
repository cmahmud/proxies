# SyndProxy private pool

## Current pool

- Alive now: 1121
- Gold now: 444
- HTTP: 403 alive / 106 gold
- HTTPS: 250 alive / 29 gold
- SOCKS4: 216 alive / 142 gold
- SOCKS5: 252 alive / 167 gold

## Historical pool

- Discovered: 152762
- Ever alive: 28391
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
