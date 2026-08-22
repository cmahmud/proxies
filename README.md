# SyndProxy private pool

## Current pool

- Alive now: 947
- Gold now: 373
- HTTP: 320 alive / 81 gold
- HTTPS: 201 alive / 23 gold
- SOCKS4: 207 alive / 138 gold
- SOCKS5: 219 alive / 131 gold

## Historical pool

- Discovered: 165836
- Ever alive: 32361
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
