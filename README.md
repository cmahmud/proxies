# SyndProxy private pool

## Current pool

- Alive now: 1062
- Gold now: 391
- HTTP: 359 alive / 84 gold
- HTTPS: 244 alive / 25 gold
- SOCKS4: 213 alive / 143 gold
- SOCKS5: 246 alive / 139 gold

## Historical pool

- Discovered: 167112
- Ever alive: 32524
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
