# SyndProxy private pool

## Current pool

- Alive now: 1008
- Gold now: 532
- HTTP: 341 alive / 159 gold
- HTTPS: 243 alive / 89 gold
- SOCKS4: 224 alive / 155 gold
- SOCKS5: 200 alive / 129 gold

## Historical pool

- Discovered: 119814
- Ever alive: 18076
- Ever gold: 714

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
