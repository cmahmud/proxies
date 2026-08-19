# SyndProxy private pool

## Current pool

- Alive now: 1150
- Gold now: 595
- HTTP: 455 alive / 182 gold
- HTTPS: 259 alive / 110 gold
- SOCKS4: 218 alive / 146 gold
- SOCKS5: 218 alive / 157 gold

## Historical pool

- Discovered: 124851
- Ever alive: 19414
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
