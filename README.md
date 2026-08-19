# SyndProxy private pool

## Current pool

- Alive now: 1033
- Gold now: 363
- HTTP: 327 alive / 67 gold
- HTTPS: 219 alive / 15 gold
- SOCKS4: 253 alive / 153 gold
- SOCKS5: 234 alive / 128 gold

## Historical pool

- Discovered: 110866
- Ever alive: 16026
- Ever gold: 507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
