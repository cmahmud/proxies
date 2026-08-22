# SyndProxy private pool

## Current pool

- Alive now: 1016
- Gold now: 394
- HTTP: 316 alive / 87 gold
- HTTPS: 214 alive / 23 gold
- SOCKS4: 243 alive / 135 gold
- SOCKS5: 243 alive / 149 gold

## Historical pool

- Discovered: 164246
- Ever alive: 32088
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
