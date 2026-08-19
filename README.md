# SyndProxy private pool

## Current pool

- Alive now: 965
- Gold now: 361
- HTTP: 309 alive / 70 gold
- HTTPS: 196 alive / 18 gold
- SOCKS4: 246 alive / 155 gold
- SOCKS5: 214 alive / 118 gold

## Historical pool

- Discovered: 110865
- Ever alive: 15989
- Ever gold: 507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
