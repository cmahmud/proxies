# SyndProxy private pool

## Current pool

- Alive now: 912
- Gold now: 367
- HTTP: 276 alive / 77 gold
- HTTPS: 216 alive / 25 gold
- SOCKS4: 205 alive / 135 gold
- SOCKS5: 215 alive / 130 gold

## Historical pool

- Discovered: 165832
- Ever alive: 32357
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
