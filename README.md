# SyndProxy private pool

## Current pool

- Alive now: 944
- Gold now: 360
- HTTP: 260 alive / 53 gold
- HTTPS: 201 alive / 16 gold
- SOCKS4: 234 alive / 150 gold
- SOCKS5: 249 alive / 141 gold

## Historical pool

- Discovered: 107085
- Ever alive: 14742
- Ever gold: 474

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
