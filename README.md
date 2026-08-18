# SyndProxy private pool

## Current pool

- Alive now: 1336
- Gold now: 214
- HTTP: 549 alive / 33 gold
- HTTPS: 272 alive / 9 gold
- SOCKS4: 292 alive / 99 gold
- SOCKS5: 223 alive / 73 gold

## Historical pool

- Discovered: 86675
- Ever alive: 6452
- Ever gold: 295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
