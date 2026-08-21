# SyndProxy private pool

## Current pool

- Alive now: 1078
- Gold now: 398
- HTTP: 362 alive / 80 gold
- HTTPS: 236 alive / 22 gold
- SOCKS4: 218 alive / 147 gold
- SOCKS5: 262 alive / 149 gold

## Historical pool

- Discovered: 158236
- Ever alive: 29975
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
