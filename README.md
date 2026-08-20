# SyndProxy private pool

## Current pool

- Alive now: 637
- Gold now: 361
- HTTP: 157 alive / 69 gold
- HTTPS: 106 alive / 21 gold
- SOCKS4: 179 alive / 131 gold
- SOCKS5: 195 alive / 140 gold

## Historical pool

- Discovered: 147017
- Ever alive: 25759
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
