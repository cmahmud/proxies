# SyndProxy private pool

## Current pool

- Alive now: 872
- Gold now: 281
- HTTP: 297 alive / 40 gold
- HTTPS: 158 alive / 9 gold
- SOCKS4: 232 alive / 137 gold
- SOCKS5: 185 alive / 95 gold

## Historical pool

- Discovered: 102895
- Ever alive: 13833
- Ever gold: 431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
