# SyndProxy private pool

## Current pool

- Alive now: 1138
- Gold now: 393
- HTTP: 374 alive / 96 gold
- HTTPS: 275 alive / 27 gold
- SOCKS4: 240 alive / 133 gold
- SOCKS5: 249 alive / 137 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25116
- Ever gold: 1054

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
