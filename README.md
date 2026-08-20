# SyndProxy private pool

## Current pool

- Alive now: 1247
- Gold now: 595
- HTTP: 458 alive / 207 gold
- HTTPS: 332 alive / 100 gold
- SOCKS4: 211 alive / 139 gold
- SOCKS5: 246 alive / 149 gold

## Historical pool

- Discovered: 138948
- Ever alive: 23395
- Ever gold: 920

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
