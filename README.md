# SyndProxy private pool

## Current pool

- Alive now: 1378
- Gold now: 550
- HTTP: 442 alive / 184 gold
- HTTPS: 351 alive / 89 gold
- SOCKS4: 239 alive / 148 gold
- SOCKS5: 346 alive / 129 gold

## Historical pool

- Discovered: 140465
- Ever alive: 23617
- Ever gold: 924

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
