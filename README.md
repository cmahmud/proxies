# SyndProxy private pool

## Current pool

- Alive now: 955
- Gold now: 363
- HTTP: 321 alive / 71 gold
- HTTPS: 171 alive / 18 gold
- SOCKS4: 248 alive / 155 gold
- SOCKS5: 215 alive / 119 gold

## Historical pool

- Discovered: 110866
- Ever alive: 16006
- Ever gold: 507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
