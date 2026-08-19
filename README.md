# SyndProxy private pool

## Current pool

- Alive now: 1017
- Gold now: 366
- HTTP: 318 alive / 67 gold
- HTTPS: 215 alive / 15 gold
- SOCKS4: 255 alive / 157 gold
- SOCKS5: 229 alive / 127 gold

## Historical pool

- Discovered: 110866
- Ever alive: 16026
- Ever gold: 507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
