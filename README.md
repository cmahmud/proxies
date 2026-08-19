# SyndProxy private pool

## Current pool

- Alive now: 990
- Gold now: 343
- HTTP: 356 alive / 71 gold
- HTTPS: 215 alive / 15 gold
- SOCKS4: 182 alive / 111 gold
- SOCKS5: 237 alive / 146 gold

## Historical pool

- Discovered: 113527
- Ever alive: 16384
- Ever gold: 514

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
