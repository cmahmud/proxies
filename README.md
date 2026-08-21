# SyndProxy private pool

## Current pool

- Alive now: 1353
- Gold now: 430
- HTTP: 523 alive / 101 gold
- HTTPS: 356 alive / 29 gold
- SOCKS4: 225 alive / 139 gold
- SOCKS5: 249 alive / 161 gold

## Historical pool

- Discovered: 159281
- Ever alive: 30410
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
