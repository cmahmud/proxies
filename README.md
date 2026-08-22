# SyndProxy private pool

## Current pool

- Alive now: 852
- Gold now: 415
- HTTP: 224 alive / 87 gold
- HTTPS: 170 alive / 24 gold
- SOCKS4: 213 alive / 145 gold
- SOCKS5: 245 alive / 159 gold

## Historical pool

- Discovered: 163327
- Ever alive: 31843
- Ever gold: 1167

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
