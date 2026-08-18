# SyndProxy private pool

## Current pool

- Alive now: 873
- Gold now: 281
- HTTP: 290 alive / 38 gold
- HTTPS: 154 alive / 9 gold
- SOCKS4: 243 alive / 139 gold
- SOCKS5: 186 alive / 95 gold

## Historical pool

- Discovered: 102895
- Ever alive: 13861
- Ever gold: 431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
