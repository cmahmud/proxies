# SyndProxy private pool

## Current pool

- Alive now: 1145
- Gold now: 424
- HTTP: 412 alive / 108 gold
- HTTPS: 286 alive / 27 gold
- SOCKS4: 218 alive / 157 gold
- SOCKS5: 229 alive / 132 gold

## Historical pool

- Discovered: 153127
- Ever alive: 28447
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
