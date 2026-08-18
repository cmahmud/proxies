# SyndProxy private pool

## Current pool

- Alive now: 992
- Gold now: 319
- HTTP: 292 alive / 35 gold
- HTTPS: 218 alive / 10 gold
- SOCKS4: 246 alive / 142 gold
- SOCKS5: 236 alive / 132 gold

## Historical pool

- Discovered: 107013
- Ever alive: 14238
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
