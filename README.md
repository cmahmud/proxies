# SyndProxy private pool

## Current pool

- Alive now: 1389
- Gold now: 433
- HTTP: 527 alive / 93 gold
- HTTPS: 313 alive / 23 gold
- SOCKS4: 238 alive / 149 gold
- SOCKS5: 311 alive / 168 gold

## Historical pool

- Discovered: 136209
- Ever alive: 22423
- Ever gold: 898

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
