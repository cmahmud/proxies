# SyndProxy private pool

## Current pool

- Alive now: 1098
- Gold now: 523
- HTTP: 436 alive / 180 gold
- HTTPS: 266 alive / 98 gold
- SOCKS4: 202 alive / 116 gold
- SOCKS5: 194 alive / 129 gold

## Historical pool

- Discovered: 124851
- Ever alive: 19406
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
