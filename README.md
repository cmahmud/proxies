# SyndProxy private pool

## Current pool

- Alive now: 884
- Gold now: 276
- HTTP: 294 alive / 37 gold
- HTTPS: 151 alive / 9 gold
- SOCKS4: 254 alive / 138 gold
- SOCKS5: 185 alive / 92 gold

## Historical pool

- Discovered: 102895
- Ever alive: 13879
- Ever gold: 431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
