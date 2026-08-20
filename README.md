# SyndProxy private pool

## Current pool

- Alive now: 1419
- Gold now: 609
- HTTP: 549 alive / 198 gold
- HTTPS: 397 alive / 101 gold
- SOCKS4: 227 alive / 145 gold
- SOCKS5: 246 alive / 165 gold

## Historical pool

- Discovered: 138956
- Ever alive: 23408
- Ever gold: 920

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
