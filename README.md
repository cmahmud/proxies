# SyndProxy private pool

## Current pool

- Alive now: 888
- Gold now: 415
- HTTP: 233 alive / 95 gold
- HTTPS: 188 alive / 23 gold
- SOCKS4: 211 alive / 138 gold
- SOCKS5: 256 alive / 159 gold

## Historical pool

- Discovered: 151678
- Ever alive: 27593
- Ever gold: 1100

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
