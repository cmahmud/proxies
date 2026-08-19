# SyndProxy private pool

## Current pool

- Alive now: 1088
- Gold now: 549
- HTTP: 408 alive / 177 gold
- HTTPS: 273 alive / 116 gold
- SOCKS4: 207 alive / 120 gold
- SOCKS5: 200 alive / 136 gold

## Historical pool

- Discovered: 124841
- Ever alive: 19305
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
