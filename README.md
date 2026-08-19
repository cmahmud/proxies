# SyndProxy private pool

## Current pool

- Alive now: 1241
- Gold now: 387
- HTTP: 414 alive / 89 gold
- HTTPS: 282 alive / 19 gold
- SOCKS4: 246 alive / 138 gold
- SOCKS5: 299 alive / 141 gold

## Historical pool

- Discovered: 133961
- Ever alive: 21621
- Ever gold: 886

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
