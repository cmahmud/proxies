# SyndProxy private pool

## Current pool

- Alive now: 996
- Gold now: 360
- HTTP: 324 alive / 53 gold
- HTTPS: 199 alive / 14 gold
- SOCKS4: 224 alive / 142 gold
- SOCKS5: 249 alive / 151 gold

## Historical pool

- Discovered: 107131
- Ever alive: 14889
- Ever gold: 478

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
