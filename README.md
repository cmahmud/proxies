# SyndProxy private pool

## Current pool

- Alive now: 897
- Gold now: 279
- HTTP: 308 alive / 38 gold
- HTTPS: 155 alive / 9 gold
- SOCKS4: 244 alive / 139 gold
- SOCKS5: 190 alive / 93 gold

## Historical pool

- Discovered: 102895
- Ever alive: 13870
- Ever gold: 431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
