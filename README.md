# SyndProxy private pool

## Current pool

- Alive now: 1297
- Gold now: 522
- HTTP: 499 alive / 178 gold
- HTTPS: 349 alive / 57 gold
- SOCKS4: 198 alive / 124 gold
- SOCKS5: 251 alive / 163 gold

## Historical pool

- Discovered: 125671
- Ever alive: 19664
- Ever gold: 775

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
